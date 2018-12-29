
#set -x
db=$1
shift
# for f in "$@"; do echo "FILE $f" > /dev/tty ; done
for f in "$@" ; do echo "FILE $f" > /dev/tty ; sed -e '/^[# \t]/d' $f ; done | sqlite3 $db '.read import.txt'
