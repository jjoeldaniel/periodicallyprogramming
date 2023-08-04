---
title: Intro to Rust
date: 2023-04-13
tags: [rust, programming]
description: A brief introduction to Rust programming.
---

## Introduction

Hello, I'm Joel, and today we're going to dive into the fascinating world of Rust programming! If you're new to Rust, you're in for a treat. Rust is a modern, systems programming language that is designed to be safe, concurrent, and fast. In this blog post, we'll cover the basics of Rust, including installation, key concepts, our first program, and some resources to help you get started.

## Setup

Getting Rust up and running on your machine is easy and quick. To install Rust, simply head to the official [Rust website](https://www.rust-lang.org/tools/install) and follow the installation instructions for your operating system. Rust has excellent support for Windows, macOS, and Linux, making it accessible to a wide range of developers.

Once Rust is installed, you'll have access to the Rust compiler, cargo, which is Rust's built-in package manager, and a powerful set of tools for building and managing Rust projects.

## Key Concepts

Rust has a unique syntax that blends C-like and functional programming paradigms. Some key concepts to understand when starting with Rust are:

-   **Variables and Data Types:** Rust has a strong static type system that helps prevent runtime errors. You'll learn how to declare and use variables, as well as work with basic data types such as integers, floats, booleans, and strings.

-   **Control Flow:** Rust provides familiar control flow statements like if/else, loops, and pattern matching to help you write expressive and efficient code.

-   **Functions:** Rust supports the creation of reusable functions, including the ability to define your own custom functions, pass arguments, and return values.

-   **Error Handling:** Rust has a unique approach to error handling that encourages developers to handle errors explicitly, which leads to more robust and reliable code.

-   **Ownership and Borrowing:** Rust's ownership system is one of the most unique features of the language. It helps prevent memory leaks and dangling pointers, and enables Rust to provide memory safety guarantees without a garbage collector.

-   **Modules and Crates:** Rust's module system allows you to organize your code into logical units, and crates are Rust's package manager and build system.

## Hello World

To get started, let's write our first Rust program. In your terminal, create a new project using cargo:

```bash
cargo new hello_world
```

From here, you can open the project in your favorite editor. The project structure should look something like this:

```bash
hello_world
├── Cargo.toml
└── src
    └── main.rs
```

The Cargo.toml file contains metadata about the project, including the project name, version, authors, and dependencies. The src directory contains the source code for the project, and the main.rs file is the entry point for the program.

Let's open main.rs and write our first Rust program:

```rust
fn main() {
    println!("Hello, world!");
}
```

Let's talk a bit about what these two lines do. The first line defines a function named main that takes no arguments and returns nothing. The second line prints the string "Hello, world!" to the console.

Pretty simple, right? Let's run the program:

```bash
cargo run
```

You should see the following output:

```
Hello, world!
```

Congratulations! You've just written your first Rust program. Let's build on this program and learn a bit more about Rust.

We are now going to cover variables and data types, as well as f strings.

In our `main.rs` file, we are going to add the following code:

```rust
fn main() {
    let x = 5;
    let y = 10;
    println!("x = {} and y = {}", x, y);
}
```

This code declares two variables, `x` and `y`, and assigns them the values `5` and `10`, respectively. The `println!` macro prints the values of `x` and `y` to the console.

Let's run the program:

```bash
cargo run
```

You should see the following output:

```bash
x = 5 and y = 10
```

Rust has a strong static type system that helps prevent runtime errors. The compiler can infer the type of a variable based on the value you assign to it. In the example above, the compiler infers that `x` is an integer and `y` is an integer. You can also explicitly declare the type of a variable by adding a colon and the type after the variable name. For example, the following code declares `x` as an integer and `y` as a float:

```rust
fn main() {
    let x: i32 = 5;
    let y: f64 = 10.0;
    println!("x = {} and y = {}", x, y);
}
```

Rust has a number of built-in data types, including integers, floats, booleans, and strings. You can find a complete list of Rust's built-in data types [here](https://doc.rust-lang.org/std/primitive/index.html).

Rust also provides a number of useful data structures, including tuples, arrays, and vectors. You can find a complete list of Rust's data structures [here](https://doc.rust-lang.org/std/collections/index.html).

## Summary

This was the first of a series of blog posts that will cover the basics of Rust. In this post, we covered how to install Rust, key concepts, and our first program. In the next post, we'll cover control flow, including if/else, loops, and pattern matching.

See you next time!

## Resources

[Comprehensive Rust](https://google.github.io/comprehensive-rust/) - Google-developed 4-day Rust crash course

[Rust by Example](https://doc.rust-lang.org/rust-by-example/) - A collection of runnable examples that illustrate various Rust concepts and standard libraries.

[Rust Book](https://doc.rust-lang.org/book/) - An introductory book about Rust. I highly recommend using this alongside the Rust by Example and Rustlings.

[Rustlings](https://github.com/rust-lang/rustlings/) - Small exercises to get you used to reading and writing Rust code!
