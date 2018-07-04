# comp
Very simple string comparison from the command line.

I made this for making sure checksums were equal, I found it a little more convenient than using 'diff' for it.

## Download
Clone
```
git clone https://github.com/Lasyin/simple_string_compare.git
```

You may need to give execution access
```
sudo chmod +x comp.py
```

Link to /usr/bin/local for ease of use (optional)
```
ln -s /path/to/repo/simple_string_compare/comp.py /usr/local/bin/comp
```

### Prerequisites
* Python

### Running
* Example of checking a SHA256 checksum
```
comp "`openssl sha -sha256 applicationName.dmg`" f24y8fb4282yh38e2h3f2iu4n
```
Now this will return false because openssl sha returns some extra print.
Use the '-cut' argument to filter this stuff out.
```
comp "`openssl sha -sha256 applicationName.dmg`" f24y8fb4282yh38e2h3f2iu4n -cut "SHA256(applicationName.dmg)= "
```
This will return true if equal.

* Example of checking an md5 checksum
```
comp "`md5 applicationName.dmg`" f349nfm349f2jd9823j -cut "MD5 (applicationName.dmg) = "
```

### Arguments
**Required**
```
str1
```
First string to compare
```
str2
```
Second string to compare

**Optional**
```
-cut
```
Substring to filter out of search result (useful for checksum output)

### Author
Bryan Collins
