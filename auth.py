import hashlib, binascii
import ldap


def check_credentials(user, passwd):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    con = ldap.initialize("ldap://localhost:7389")
    con.simple_bind_s('cn=admin,dc=sfn,dc=intranet', open("/etc/ldap.secret", "r").read())
    try:
        pwd_hash_db = con.search_s('dc=sfn,dc=intranet', ldap.SCOPE_SUBTREE, 'uid=%s' % user)[0][1]['sambaNTPassword'][
            0]
    except IndexError:
        pwd_hash_db = ""  # user does not exist

    pwd_hash_user = binascii.hexlify(hashlib.new('md4', passwd.encode('utf-16le')).digest()).upper()
    con.unbind_s()
    return pwd_hash_user == pwd_hash_db


def get_name(user):
    return "Jaro"
