#!/usr/bin/env python
import ConfigParser
import string, os, sys
import getpass

def checkout_repository(name, url, branch, headid, files, user, passwd):
    command = "meta-ubinux/scripts/checkoutrepos.sh"
    command = command + " " + name
    command = command + " " + url
    command = command + " " + branch
    command = command + " " + headid
    command = command + " \"" + files + "\""
    command = command + " " + user
    command = command + " " + passwd

    os.system(command)

def checkout_all_repository():
    cf = ConfigParser.ConfigParser()
    cf.read("meta-ubinux/conf/depend.metas")
    sec = cf.sections()

    metas = cf.get("DEPEND_META", "metas")
    saved_ipstr = ''

    print '------------------------------------------------------------'
    username = raw_input('Please enter username@' + saved_ipstr + ': ')
    passwd = getpass.getpass('Password: ')
    print '------------------------------------------------------------'

    for meta in metas.split():
        giturl = cf.get(meta, "GITURL")
        branch = cf.get(meta, "BRANCH")
        headid = cf.get(meta, "HEADID")
        files  = cf.get(meta, "FILES")

        checkout_repository(meta, giturl, branch, headid, files, username, passwd)


def main():
    if len(sys.argv) == 1:
        checkout_all_repository()
    else:
        cf = ConfigParser.ConfigParser()
        cf.read("meta-ubinux/conf/depend.metas")
        sec = cf.sections()
        metas = cf.get("DEPEND_META", "metas")

        for i in range(1, len(sys.argv)):
            for meta in metas.split():
                if sys.argv[i] == meta:
                    giturl = cf.get(meta, "GITURL")
                    branch = cf.get(meta, "BRANCH")
                    headid = cf.get(meta, "HEADID")
                    files  = cf.get(meta, "FILES")

                    print '------------------------------------------------------------'
                    username = raw_input('Please enter username@' + ipstr + ': ')
                    passwd = getpass.getpass('Password: ')
                    print '------------------------------------------------------------'

                    checkout_repository(meta, giturl, branch, headid, files, username, passwd)

if __name__ == "__main__":
    try:
        ret = main()
    except Exception:
        ret = 1
        import traceback
        traceback.print_exc(5)
    sys.exit(ret)

