# zippy-quotes

YOW!! A list of some CLASSIC quotes from the ZIPPY THE PINHEAD [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)) file.

PRs welcome.

## Install

```sh
npm install zippy-quotes [--g|--save]
```

## Example

This module comes in an API and CLI. Example in code:

```js
var zippy = require('zippy-quotes')

// random quote
console.log(zippy())
//=> '"DARK SHADOWS" is on!! Hey, I think the VAMPIRE forgot his UMBRELLA!!'

// the array of all quotes
console.log(zippy.quotes)
```

## Usage

[![NPM](https://nodei.co/npm/zippy-quotes.png)](https://www.npmjs.com/package/zippy-quotes)

### API

#### `quote = zippy()`

Returns a random quote string, like `'I'm CONTROLLED by the CIA!! EVERYONE is controlled by the CIA!!'`.

#### `list = zippy.quotes`

The array of all quotes.

#### `list = require('zippy-quotes/quotes.json')`

The full JSON array.

### CLI

You can also use the CLI here.

```
Usage:
  zippy-quotes [opt]
  
Options:
  --help  show help
  --all   list all quotes, separated by newlines
```

Example:

```sh
$ zippy-quotes
I just forgot my whole philosophy of life!!!
```

## License

LNT, see [LICENSE.md](http://github.com/julescarbon/zippy-quotes/blob/master/LICENSE.md) for details.
