# postman fundamentals course pluralsight

## Links

- [Postman JavaScript reference | Postman Learning Center](https://learning.postman.com/docs/writing-scripts/script-references/postman-sandbox-api-reference/)
- [Scripting in Postman | Postman Learning Center](https://learning.postman.com/docs/writing-scripts/intro-to-scripts/)
- [Test script examples | Postman Learning Center](https://learning.postman.com/docs/writing-scripts/script-references/test-examples/#getting-started-with-tests)
- [Test script examples | Postman Learning Center](https://learning.postman.com/docs/writing-scripts/script-references/test-examples/#validating-response-structure)

## Postman basics

Clone repo <https://github.com/taylonr/postman>

Dependencies

```
npm install

```

Run server

```bash
cd C:\Users\MaksimZinovev\repos\postman
npm run start:dev
to restart at any time, enter `rs`

```

Open in browser: <http://localhost:3000/landing>

## Visualiser in Postman

Add code in Tests tab

```js
var template = `
    <table bgcolor="#FFFFFF">
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>ISBN</th>
        </tr>

        {{#each response}}
            <tr>
                <td>{{id}}</td>
                <td>{{title}}</td>
                <td>{{author}}</td>
                <td>{{isbn}}</td>
            </tr>
        {{/each}}
    </table>
`;

// Set visualizer
pm.visualizer.set(template, {
    // Pass the response body parsed as JSON as `data`
    response: pm.response.json()
});


```

## Using history section

## Changing GET requests to POST

Authentication required: admin

Body: no

## Preset headers

Example:

- required headers
  - username
  - password
  - business unit
  - client id
  - authorization

## Header presets

Request > Headers > Presets > Add new preset

Now create new request > Headers > Presets > Your preset.

## Environments

create
replace hardcoded values with environment variable
duplicate
view icon (top right)

## Import

```
http://localhost:3000/ui

```

Go to browser
Create new book
Network tab > Copy as cURL
Postman > Import > Raw test > paste > Import

## Proxy

Postman > Bottom right > Capture requests > Enable proxy > <https://learning.postman.com/docs/sending-requests/capturing-request-data/capturing-https-traffic/#installing-openssl-on-windows>

Postman >  Bottom right > Capture requests > Start capture

Install Chrome extension

Go to browser and interaact with web app

## Generating  code

Send request
Right side of window > Code snippet

## Sync

Allows to sync between multiple computers

## Pre-built tests

Send request
Tests tab  
Snippets
Response > Test results

## Test syntax

pm
.info
.globals
.environment
.assertions

Status code is 200

```js
pm.test("Status code name has string", () => {
    pm.response.to.have.status("OK");
});

```


## Basic tests 

```js 
pm.test("All books should have a title", () => {
    const books = pm.response.json();
    pm.expect(books.every(book => {
        return book.title !== undefined;
    })).to.be.true;
});

```


Refactored 

```js 

const titleIsDefined = (book) => {
    return book.title !== undefined;
}

pm.test("All books should have a title", () => {
    const books = pm.response.json();
    pm.expect(books.every(titleIsDefined)).to.be.true;
});

```

## Using other libraries 

```js 

const moment  = require('moment');

obj = {
    "title": `${pm.variables.replaceIn('{{$randomWords}}')}`,
    "author": `${pm.variables.replaceIn('{{$randomFirstName}}')}`,
    "isbn": `${pm.variables.replaceIn('{{$randomInt}}')}743351Y`,
    "releaseDate": `${moment().format('YYYY-MM-DD')}`
}

pm.collectionVariables.set('book', JSON.stringify(obj));

```
Test 

```js 

const moment = require('moment'); 
pm.test('Create date is equal to today', () => {
    const data = pm.response.json();
    pm.expect(moment(data.createdAt).format('MM/DD/YYYY'))
    .to.eql(moment().format('MM/DD/YYYY'))
})

```

## Creating collections 


Create collection and add request.

POST http://localhost:3000/households

```cURL

curl --location 'http://localhost:3000/households' \
--header 'Content-Type: application/json' \
--header 'G-TOKEN: ROM831ESV' \
--data '{
    "name": "Max Household"
}'

```

Create users request 
POST

```curl 

curl --location 'http://localhost:3000/users' \
--header 'Content-Type: application/json' \
--header 'G-TOKEN: ROM831ESV' \
--data-raw '{
    "email": "troytiru+pm07@gmail.com", 
    "firstName": "Max1",
    "lastName": "Zin1",
    "householdId": 1
}'

```

Add book to whishlist 

POST 

```curl 

curl --location 'http://localhost:3000/wishlists/1/books/1' \
--header 'Content-Type: application/json' \
--header 'G-TOKEN: ROM831ESV' \
--data-raw '{
    "email": "troytiru+pm07@gmail.com", 
    "firstName": "Max1",
    "lastName": "Zin1",
    "householdId": 1
}'

```

GET household books 

```curl

curl --location 'http://localhost:3000/households/1/wishlistBooks' \
--header 'Content-Type: application/json' \
--header 'G-TOKEN: ROM831ESV' \
--data ''

```

To set Variable
1. Send request 
2. Tests > Snippets > Set global variable 