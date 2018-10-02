"""
DevSend.

Usage: devsend [ --to ACCT ] [ --help | --info ] [ --from ACCOUNT ] [ --pass PASSWORD ] [ --value VALUE ] [ --host HOST ] [ --port PORT ]


--help              Print this message.
--info              Print run requirement information.s
--to ACCT           Account to send value to.
--from ACCOUNT      Account to send value from.[default: 0x00a329c0648769a73afac7f9381e08fb43dbea72]
--pass PASSWORD     Password of the sending account.[default: None]
--value VALUE       Amount to send in GWEI[default: 0x1000000000000]
--host HOST         Host of the node.[default: 127.0.0.1]
--port PORT         Port of the node.[default: 8545]
"""
if __name__ == "__main__":
    import docopt
    import requests
    import sys

    NOTES = '\
    Notes:\n\
    in order to use this script run parity as follows:\n\
    \n\
    parity --chain dev --jsonrpc-apis all\n\
    \n\
    This script will send value from the default dev account to the\n\
    account named in --to with value being sent as --amount'

    #parses the cli input options
    kwargs = docopt.docopt(__doc__)

    for key in list(kwargs.keys()):
        kwargs[key.replace('--','')] = kwargs[key]
        del kwargs[key]

    if kwargs["info"]:
        print(NOTES)
        sys.exit(0)

    if kwargs["pass"] == "None":
        kwargs["pass"]=""

    transaction = {"params":[],"jsonrpc":"2.0","id":0}
    transaction["method"] = "personal_sendTransaction"
    transaction["params"]=[{"to":kwargs["to"],"from":kwargs["from"],"value":kwargs["value"]},kwargs["pass"]]
    r=requests.post('http://{}:{}'.format(kwargs["host"],kwargs["port"]),json=transaction)
    print(r.text)
