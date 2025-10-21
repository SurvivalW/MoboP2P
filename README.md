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
│   └── settings.toml         # Global configuration
│
├── data/
│   ├── keys/                 # Private/public keypairs for identity
│   └── messages/             # Message queue and history (encrypted)
│
├── docs/                     # Documentation for usage and protocol
│   └── protocol.md
|
├── scripts/                  # Helper scripts
│   └── generate_keys.py
|
├── src/
│   ├── network/              # Networking layer
│   │   ├── connection.py     # Peer connection management
│   │   ├── handshake.py      # Key exchange, authentication, session setup
│   │   └── framing.py        # Message framing
│   │
│   ├── crypto/               # Encryption & signing
│   │   ├── key_management.py # Key generation, storage, rotation
│   │   ├── encrypt.py        # AEAD encrypt/decrypt messages
│   │   └── sign.py           # Sign messages, verify signatures
│   │
│   ├── messaging/            # Core messaging logic
│   │   ├── send.py           # Queue messages and send
|   |   ├── style.css         # Style for the TUI
│   │   └── receive.py        # Validate and decrypt messages
│   │
│   ├── bootstrap/            # Optional peer discovery / relay
│   │   └── bootstrap.py      # Maintain known peer list, NAT traversal
│   │
│   └── main.py               # Entry point: combines networking, messaging, crypto, TUI the whole shabang😉
│
├── tests/                    # Unit & integration tests
│   ├── test_network.py
│   ├── test_crypto.py
│   └── test_messaging.py
│
│
├── README.md                 # What you reading right now
├── requirements.txt          # What you need to run my app
└── setup.py                  # Packaging and installation configuration
```


## ❤️ Support MoboP2P

If you enjoy using MoboP2P and want to support development, you can send a few sats (Bitcoin). Your support is completely optional and helps keep the project going!

Lighting:
![BTC](https://github.com/user-attachments/assets/cdb814cb-acef-4af1-8699-09bcedba4b11)
On-Chain:
bc1pa2ptetj6ax4y9m367tlr2wc9nq3t3mnwl90cq2x5c2as06zw4apsvmc7v5
