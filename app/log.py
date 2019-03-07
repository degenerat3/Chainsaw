
def log(string):
    """
    Write the supplied string to the input.log file
    @param string: data to be writte to log file (newlines included)
    @return: None
    """
    with open('/tmp/reach/logs/input.log', 'a') as f:
        f.write(string.rstrip() + "\n")
    return True


def log_fw(ip, rules):
    """
    Take in string, which will be all iptables-save output, split it into one rule per line, log in form:
    <IP>      <RULE>
    so each line of log file has one rule
    @param ip: The source IP address, will be used as identifer
    @param rules: the output of all the iptables-save command (including newlines)
    @return: None    
    """
    lines = ""
    # Loop through all the rules and rebuild the command used to insert the rule
    current_table = ""  # The current iptables table we are in
    for line in rules.split("\n"):
        line = line.strip()
        # Skip COMMIT, Comments, empty lines, and the :CHAINS
        if not line:
            continue
        if line.lstrip().startswith("COMMI"):
            continue
        if line.lstrip().startswith("#"):
            continue
        if line.lstrip().startswith(":"):
            continue
        if line.lstrip().startswith("*"):
            current_table = line.lstrip("*")
            continue
        lines += "{} iptables -t {} {}\n".format(ip, current_table, line)
    log(lines)
    

def log_hosts(ip, hosts):
    """
    Take in string, which will be the /etc/hosts file, split it into one host per line, log in form:
    <IP>      HOSTS[6]        <host_ip>       <hostname>
    so each line of log file has "host" entry
    @param ip: The source IP address, will be used as identifer
    @param hosts: the output of "cat /etc/hosts" (including newlines)
    @return: None    
    """
    def is_hostname_local(hostname):
        # Skip certain default host values
        values = ["loopback", "localhost", "ip6-localnet", "ip6-mcastprefix", "ip6-allnodes", "ip6-allrouters"]
        for v in values:
            if v in hostname:
                return True
        return False
    
    lines = ""
    for line in hosts.split("\n"):
        line = line.strip()
        # Skip Comments, empty lines
        if not line:
            continue
        if line.lstrip().startswith("#"):
            continue
        try:
            # Put each hostname on its own line
            addr, *hosts = line.split()
            # Detect if IPv4 or IPv6
            if addr.count(".") == 3:
                typ = "HOSTS"
            elif addr.count(":") >= 2:
                typ = "HOSTS6"
            else:
                # We _should_ never get this, who knows
                typ = "HOSTS_UNKNOWN"
            for hostname in hosts:
                hostname = hostname.lower()
                if is_hostname_local(hostname):
                    continue
                lines += "{} {} {} {}\n".format(ip, typ, addr, hostname)
        except ValueError:
            continue
    log(lines)
    return


def log_routes(ip, routes):
    """
    Take in string, which will be all ip routes output, split it into one route per line, log in form:
    <IP>      ROUTE        <Route Data>
    so each line of log file has one route
    @param ip: The source IP address, will be used as identifer
    @param routes: the output of the "ip route" (including newlines)
    @return: None    
    """
    lines = ""
    for route in routes.split("\n"):
        route = route.strip()
        lines += "{} ROUTE {}\n".format(ip, route)
    log(lines)
    return


def log_creds(ip, creds):
    """
    Take in cred string, which will be format: "type:user:pass\ntype:user:pass\n", parse into:
    <IP>      CREDENTIAL      <type:user:pass>
    so each line has one credential set
    @param ip: The source IP address, will be used as identifier
    @param creds: all collected credentials in one string, newlines included
    @return: None
    """
    lines = ""
    lines = ""
    for line in creds.split("\n"):
        splt = line.split(":", 2)
        typ = splt[0]
        user = splt[1]
        pswd = splt[2]
        lines += "{} CREDENTIAL {} {} {}\n".format(ip, typ, user, pswd)
    log(lines)
    return
