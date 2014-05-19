# Carbon Client

This simple carbon client is able to send data via

* the plaintext
* the pickle

protocol into carbon.

## Pre-requisites

You'll need to install a python few modules, including:

* socket
* struct
* cPickle
* sys

## Usage

Example for the plaintext protocol:

	import time
	from carbon_client import CarbonClient
	
	carbon = CarbonClient(args.carbon_host, args.carbon_port)

	carbon.send_plaintext(name, float(value), int( time.time() ))

Example for the pickle protocol:

	import time
	from carbon_client import CarbonClient
	
	carbon = CarbonClient(args.carbon_host, args.carbon_port)
	
	pickle = []
	
	now = int( time.time() )
	
	pickle.append(name1, (now, str( value1 )))
	pickle.append(name2, (now, str( value2 )))
	
	carbon.send_pickle(pickle)

## License and Authors

Author:: Andreas Rütten (andreas@smaato.com)

Copyright:: 2013, Smaato, Inc.

Licensed under the  MIT License (MIT)

	 Permission is hereby granted, free of charge, to any person
	 obtaining a copy of this software and associated
	 documentation files (the "Software"), to deal in the Software
	 without restriction, including without limitation the rights
	 to use, copy, modify, merge, publish, distribute, sublicense,
	 and/or sell copies of the Software, and to permit persons to
	 whom the Software is furnished to do so, subject to the
	 following conditions:

	 The above copyright notice and this permission notice shall
	 be included in all copies or substantial portions of the Software.

	 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
	 KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
	 WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
	 PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
	 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
	 OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
	 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contributing

We welcome contributed improvements and bug fixes via the usual github
workflow:

1. Fork this repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new pull request
