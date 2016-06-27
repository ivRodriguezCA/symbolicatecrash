# symbolicatecrash
Manually symbolicate iOS crashes

## Usage:
```python
python symbolicatecrash.py -n <app_name> -c <crash_report> -a <architecture>
```

## Assumptions:
To make the parameters very simple, `symbolicatecrash` only expects the *App Name* and assumes the following:
- There is a .app package in the same directory with a binary file named exactly the same: **\<app_name>.app/\<app_name>**
- There is a .dSYM package named **\<app_name>.app.dSYM**

License
----

The MIT License (MIT)
Copyright (c) 2016 Ivan Rodriguez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[ec-type]: <http://opensource.apple.com/source/Security/Security-55471/sec/Security/SecECKey.c>
[IRPublicConstants-header]: <https://github.com/ivRodriguezCA/IRCrypto/blob/master/IRCrypto/IRPublicConstants.h>
[Authenticated-Encryption]: <https://en.wikipedia.org/wiki/Authenticated_encryption>
[Advanced-Encryption-Standard]: <https://en.wikipedia.org/wiki/Advanced_Encryption_Standard>
[Cipher-Block-Chaining]: <https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29>
[Hash-Based-Message-Authentication-Code]: <https://en.wikipedia.org/wiki/Hash-based_message_authentication_code>
[RNCryptor-File-Format-v3]: <https://github.com/RNCryptor/RNCryptor-Spec/blob/master/RNCryptor-Spec-v3.md>
