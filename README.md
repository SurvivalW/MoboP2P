# MoboP2P

## Mission

The mission of this project is simple: to create the **most secure messaging application for the terminal**.  

In a world where privacy is constantly under threat, and modern messaging platforms trade security for convenience and tracking, this project aims to put control back in the hands of the user. Every message and every connection is designed with security, privacy, and reliability as the absolute priority.  

By combining **end-to-end encryption** and **peer-to-peer communication**, this messenger ensures that users can communicate confidently and directly, without exposing sensitive information to third parties.  

This project is for those who demand security without compromise, who value privacy, and who prefer the terminal as their command center. Every design decision reflects this philosophy: **simplicity, transparency, and unyielding security**.

## File Structure

```
MoboP2P/
│
├── config/
│   └── settings.toml         # Global configuration (ports, peer list, logging)
│
├── data/
│   ├── keys/                 # Private/public keypairs for identity
│   └── messages/             # Message queue and history (encrypted)
│
├── src/
│   ├── network/              # Networking layer
│   │   ├── connection.py     # Peer connection management
│   │   ├── handshake.py      # Key exchange, authentication, session setup
│   │   └── framing.py        # Message framing (length prefix, sequencing)
│   │
│   ├── crypto/               # Encryption & signing
│   │   ├── key_management.py # Key generation, storage, rotation
│   │   ├── encrypt.py        # AEAD encrypt/decrypt messages
│   │   └── sign.py           # Sign messages, verify signatures
│   │
│   ├── messaging/            # Core messaging logic
│   │   ├── send.py           # Queue messages and send
│   │   ├── receive.py        # Validate and decrypt messages
│   │   └── ui.py             # Terminal input/output handling
│   │
│   ├── bootstrap/            # Optional peer discovery / relay
│   │   └── bootstrap.py      # Maintain known peer list, NAT traversal
│   │
│   └── main.py               # Entry point: combines networking, messaging, crypto
│
├── tests/                    # Unit & integration tests
│   ├── test_network.py
│   ├── test_crypto.py
│   └── test_messaging.py
│
├── scripts/                  # Helper scripts (key generation, message inspection)
│   └── generate_keys.py
│
├── docs/                     # Documentation for usage and protocol
│   └── protocol.md
│
├── README.md
└── requirements.txt
```




## <3
### If you'd like to show your support, send a few sats XD
![Bitcoin](/BTC.jpg)
