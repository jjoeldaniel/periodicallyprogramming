## Introduction

The purpose of this blog post is to introduce developers to the use of Markdown for sharing code with others and explores alternative tools like Pastebin and Privatebin. 

This is specifically oriented towards use on Discord, however any site that supports [Markdown's extended syntax elements](https://www.markdownguide.org/extended-syntax/) will also work.

## Structuring

Before anyone can dive into reviewing your code, it has to actually be readable and structured clearly.

<small>This means not submitting this when asking for help</small>

![code](https://ak.picdn.net/shutterstock/videos/24896750/thumb/12.jpg?ip=x480)

Typically, the best way to directly post your code is with [fenced code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) from Markdown.

Instead of posting a wall of text, we can use these blocks to structure our code in a nice, easy-to-understand way (we even have access to syntax highlighting).

### Example:

<small>In this case, the language is JSON, replace `json` with the actual language you are using</small>

`````
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
`````

...would produce:

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

This way we can directly post our code. However, it's not always the best solution for large chunks of code. For this, I would recommend tools such as [Pastebin](https://pastebin.com/) or [Privatebin](https://privatebin.net/). Of course, if your code is already on GitHub, feel free to link that too!

You can find an example of Pastebin in action [here](https://pastebin.com/qzBQxvwb).

## Summary

This blog post provides useful tips for developers looking to share their code with others in a clear and organized way, using the tools and features of Markdown. Hopefully, you've learned a thing or two about Markdown!

## Resources

* [Markdown Guide](https://www.markdownguide.org/extended-syntax/)
* [Pastebin](https://pastebin.com/)
* [Privatebin](https://privatebin.net/)
