# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 was to investigate the foundational principles of computer networking: defining and contextualizing fundamental network architectures (LAN, MAN, WAN) and protocols, performing hands-on network reachability tests (`ping`) and domain name resolution (`nslookup`), and constructing a rigorous, step-by-step technical explanation of the end-to-end client-server lifecycle when opening a website in a browser.

---

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Concrete Real-World Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network that interconnects computers and peripherals within a restricted, localized physical space such as a home, school laboratory, or office suite. | A home Wi-Fi network connecting a laptop, smartphone, smart TV, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A larger network infrastructure spanning an entire city, municipality, or extensive multi-campus university facility, bridging multiple LANs together. | The Bengaluru city municipal fiber network connecting traffic cameras, transit systems, and civic administration offices. |
| **WAN (Wide Area Network)** | A vast telecommunications network that spans large geographic distances—spanning across cities, states, nations, or continents—interconnecting disparate LANs and MANs. | The global Internet, or an international banking network (such as the SWIFT financial messaging system). |
| **DNS (Domain Name System)** | The distributed, hierarchical directory service that translates human-friendly alphanumeric domain names into machine-routable numerical IP addresses. | Cloudflare (`1.1.1.1`) or Google (`8.8.8.8`) resolving `example.com` to `172.66.147.243`. |
| **Router** | A specialized network layer device that reads destination IP addresses on data packets and forwards them between different networks along the most efficient path. | A residential fiber ONT/Wi-Fi router directing traffic between a private local subnet (`192.168.1.0/24`) and the ISP's public network. |
| **Protocol** | A formal, standardized contract of rules, formats, syntax, and error-handling procedures that governs how electronic devices communicate without ambiguity. | **HTTPS** (Hypertext Transfer Protocol Secure) running on top of **TCP/IP** to transfer encrypted web pages. |
| **Packet switching** | A transmission method where digital data is partitioned into discrete chunks called packets, each routed independently across shared network links and reassembled at the destination. | Streaming a YouTube video where audio and video chunks travel as thousands of independent TCP/IP packets across the Internet. |
| **Client-server** | An asymmetric distributed computing model where one party (the client) initiates requests for data or services, and a centralized host (the server) listens, processes, and responds. | A web browser (client) requesting an HTML document from a GitHub web server (server). |

---

### Task 7.2 — Observe network information
I conducted network reachability and domain lookup tests using standard terminal utilities. In accordance with assignment privacy rules, all private local addresses and internal identifiers have been redacted.

#### 1. Connectivity Test:
```bash
ping -c 3 example.com
```
- **Terminal Output Observed**:
  ```text
  PING example.com (172.66.147.243): 56 data bytes
  64 bytes from 172.66.147.243: icmp_seq=0 ttl=59 time=4.511 ms
  64 bytes from 172.66.147.243: icmp_seq=1 ttl=59 time=5.759 ms
  64 bytes from 172.66.147.243: icmp_seq=2 ttl=59 time=15.010 ms

  --- example.com ping statistics ---
  3 packets transmitted, 3 packets received, 0.0% packet loss
  round-trip min/avg/max/stddev = 4.511/8.427/15.010/4.683 ms
  ```

#### 2. DNS Resolution Lookup:
```bash
nslookup example.com
```
- **Terminal Output Observed**:
  ```text
  Server:		1.1.1.1
  Address:	1.1.1.1#53

  Non-authoritative answer:
  Name:	example.com
  Address: 104.20.23.154
  Name:	example.com
  Address: 172.66.147.243
  ```

#### Questions & Observations:
- **What a connectivity test helps you check**:
  Running a connectivity test like `ping` transmits ICMP (Internet Control Message Protocol) Echo Request packets to a target host. It checks whether a complete two-way communication pathway exists between the local machine and the destination host, identifies whether intermediate routers are dropping packets (packet loss percentage), and measures network latency (round-trip time in milliseconds).
- **What information a DNS lookup displays**:
  A DNS lookup reveals the identity and port of the recursive resolver that answered the query (`1.1.1.1#53`), whether the record came from an authoritative source or an intermediate cache (non-authoritative), and the specific IPv4/IPv6 addresses (`104.20.23.154`, `172.66.147.243`) mapped to the requested domain name.
- **The role of DNS when you enter a website name in a browser**:
  Humans find words memorable (e.g., `google.com`), but computers, routers, and network switches only route packets using numerical IP addresses. When a user types a website address into a browser, DNS acts as the essential telephone directory of the Internet, resolving that hostname into an IP address so the browser knows the exact destination socket to open.

---

### Task 7.3 — What happens when you open a website?
The complete end-to-end communication lifecycle involves 6 distinct phases:

1. **Client URL Entry & Cache Check**:
   The user types `https://example.com` into the web browser (the **client**) and hits Enter. The browser first checks its own local cache, the operating system DNS cache, and local router cache to see if an IP address mapping for `example.com` is already available.
2. **DNS Resolution Protocol**:
   If the IP address is not cached, the client sends a DNS query using the **DNS protocol** (UDP port 53) to a configured resolver (e.g. `1.1.1.1`). The resolver performs hierarchical queries across Root, TLD (.com), and Authoritative nameservers, returning the destination IP address (`172.66.147.243`) to the client.
3. **TCP 3-Way Handshake & TLS Negotiation**:
   Using the resolved IP address, the client initiates a reliable connection with the remote **server** using the Transmission Control **Protocol** (TCP) via a 3-way handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`) on port 443. For HTTPS, a cryptographic TLS handshake immediately follows to verify the server's identity certificate and establish symmetric encryption keys.
4. **Packet Switching Across Network Routers**:
   The client constructs an HTTP GET request for the root document (`/`). The operating system slices this request into data packets. Multiple intermediate **routers** examine packet destination IP headers, consulting dynamic routing tables to forward each packet hop-by-hop across the Internet via packet switching.
5. **Server Processing & HTTP Response**:
   The destination web **server** receives the arrival packets, reassembles them, parses the HTTP request headers, and generates an HTTP response. It packages a `200 OK` status header along with the requested HTML payload into response packets and streams them back across the network to the client.
6. **Client Rendering & Visual Display**:
   The client browser receives and reassembles the response packets, parses the HTML DOM tree, requests referenced sub-resources (CSS stylesheets, images, JavaScript files), calculates layout geometry, and renders the finished, interactive webpage for the user.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested ICMP packet transmission, round-trip latency, and zero packet loss.
- `nslookup example.com`: Queried public DNS resolver `1.1.1.1` to inspect A record mapping.
- Network analytical models: Synthesized the OSI / TCP-IP layered model to trace website resolution.

## 4. My understanding
Computer networking is fundamentally an agreed hierarchy of abstractions. Without universal protocols (like IP, TCP, DNS, and HTTP), heterogeneous hardware from thousands of different manufacturers could never exchange intelligible information. Experiencing `ping` and `nslookup` firsthand in the terminal revealed the real physical machinery behind web surfing: the fact that even opening a single webpage involves DNS queries, TCP handshakes, packet routing across dozens of physical fiber switches, and TLS cryptographic key agreements—all executing seamlessly within a few milliseconds.

## 5. Difficulties faced
When looking up domain information, some websites use Content Delivery Networks (CDNs) like Cloudflare, which return multiple IP addresses for a single domain name, which was initially surprising.

## 6. How I resolved them
I researched multi-homed and CDN architectures, discovering that CDNs return multiple Anycast IP addresses for high availability, load balancing, and DDoS mitigation, ensuring traffic is routed to the geographically closest edge data center.

## 7. Evidence / files
- `mission-07-networking/README.md` (this report)
- Terminal execution logs for `ping` and `nslookup` (sanitized for privacy)

## 8. Commit details
- **Commit Message**: `Explain networking concepts and website communication`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
