JavaScript data types and data structures
Programming languages all have built-in data structures, but these often differ from one language to another. This article attempts to list the built-in data structures available in JavaScript and what properties they have. These can be used to build other data structures.

The language overview offers a similar summary of the common data types, but with more comparisons to other languages.

Dynamic and weak typing
JavaScript is a dynamic language with dynamic types. Variables in JavaScript are not directly associated with any particular value type, and any variable can be assigned (and re-assigned) values of all types:

let foo = 42; // foo is now a number
foo = "bar"; // foo is now a string
foo = true; // foo is now a boolean
Copy to Clipboard
JavaScript is also a weakly typed language, which means it allows implicit type conversion when an operation involves mismatched types, instead of throwing type errors.

const foo = 42; // foo is a number
const result = foo + "1"; // JavaScript coerces foo to a string, so it can be concatenated with the other operand
console.log(result); // 421
Copy to Clipboard
Implicit coercions is very convenient, but can be a potential footgun if developers didn't intend to do the conversion, or intend to convert in the other direction (for example, string to number instead of number to string). For symbols and BigInts, JavaScript has intentionally disallowed certain implicit type conversions.

Primitive values
All types except Object define immutable values represented directly at the lowest level of the language. We refer to values of these types as primitive values.

All primitive types, except null, can be tested by the typeof operator. typeof null returns "object", so one has to use === null to test for null.

All primitive types, except null and undefined, have their corresponding object wrapper types, which provide useful methods for working with the primitive values. For example, the Number object provides methods like toExponential(). When a property is accessed on a primitive value, JavaScript automatically wraps the value into the corresponding wrapper object and accesses the property on the object instead. However, accessing a property on null or undefined throws a TypeError exception, which necessitates the introduction of the optional chaining operator.

Type	typeof return value	Object wrapper
Null	"object"	N/A
Undefined	"undefined"	N/A
Boolean	"boolean"	Boolean
Number	"number"	Number
BigInt	"bigint"	BigInt
String	"string"	String
Symbol	"symbol"	Symbol
The object wrapper classes' reference pages contain more information about the methods and properties available for each type, as well as detailed descriptions for the semantics of the primitive types themselves.

Null type
The Null type is inhabited by exactly one value: null.

Undefined type
The Undefined type is inhabited by exactly one value: undefined.

Conceptually, undefined indicates the absence of a value, while null indicates the absence of an object (which could also make up an excuse for typeof null === "object"). The language usually defaults to undefined when something is devoid of a value:

A return statement with no value (return;) implicitly returns undefined.
Accessing a nonexistent object property (obj.iDontExist) returns undefined.
A variable declaration without initialization (let x;) implicitly initializes the variable to undefined.
Many methods, such as Array.prototype.find() and Map.prototype.get(), return undefined when no element is found.
null is used much less often in the core language. The most important place is the end of the prototype chain — subsequently, methods that interact with prototypes, such as Object.getPrototypeOf(), Object.create(), etc., accept or return null instead of undefined.

null is a keyword, but undefined is a normal identifier that happens to be a global property. In practice, the difference is minor, since undefined should not be redefined or shadowed.

Boolean type
The Boolean type represents a logical entity and is inhabited by two values: true and false.

Boolean values are usually used for conditional operations, including ternary operators, if...else, while, etc.

Number type
The Number type is a double-precision 64-bit binary format IEEE 754 value. It is capable of storing positive floating-point numbers between 2-1074 (Number.MIN_VALUE) and 21024 (Number.MAX_VALUE) as well as negative floating-point numbers between -2-1074 and -21024, but it can only safely store integers in the range -(253 − 1) (Number.MIN_SAFE_INTEGER) to 253 − 1 (Number.MAX_SAFE_INTEGER). Outside this range, JavaScript can no longer safely represent integers; they will instead be represented by a double-precision floating point approximation. You can check if a number is within the range of safe integers using Number.isSafeInteger().

Values outside the range ±(2-1074 to 21024) are automatically converted:

Positive values greater than Number.MAX_VALUE are converted to +Infinity.
Positive values smaller than Number.MIN_VALUE are converted to +0.
Negative values smaller than -Number.MAX_VALUE are converted to -Infinity.
Negative values greater than -Number.MIN_VALUE are converted to -0.
+Infinity and -Infinity behave similarly to mathematical infinity, but with some slight differences; see Number.POSITIVE_INFINITY and Number.NEGATIVE_INFINITY for details.

The Number type has only one value with multiple representations: 0 is represented as both -0 and +0 (where 0 is an alias for +0). In practice, there is almost no difference between the different representations; for example, +0 === -0 is true. However, you are able to notice this when you divide by zero:

console.log(42 / +0); // Infinity
console.log(42 / -0); // -Infinity
Copy to Clipboard
NaN ("Not a Number") is a special kind of number value that's typically encountered when the result of an arithmetic operation cannot be expressed as a number. It is also the only value in JavaScript that is not equal to itself.

Although a number is conceptually a "mathematical value" and is always implicitly floating-point-encoded, JavaScript provides bitwise operators. When applying bitwise operators, the number is first converted to a 32-bit integer.

Note: Although bitwise operators can be used to represent several Boolean values within a single number using bit masking, this is usually considered a bad practice. JavaScript offers other means to represent a set of Booleans (like an array of Booleans, or an object with Boolean values assigned to named properties). Bit masking also tends to make the code more difficult to read, understand, and maintain.

It may be necessary to use such techniques in very constrained environments, like when trying to cope with the limitations of local storage, or in extreme cases (such as when each bit over the network counts). This technique should only be considered when it is the last measure that can be taken to optimize size.

BigInt type
The BigInt type is a numeric primitive in JavaScript that can represent integers with arbitrary magnitude. With BigInts, you can safely store and operate on large integers even beyond the safe integer limit (Number.MAX_SAFE_INTEGER) for Numbers.

A BigInt is created by appending n to the end of an integer or by calling the BigInt() function.

This example demonstrates where incrementing the Number.MAX_SAFE_INTEGER returns the expected result:

// BigInt
const x = BigInt(Number.MAX_SAFE_INTEGER); // 9007199254740991n
x + 1n === x + 2n; // false because 9007199254740992n and 9007199254740993n are unequal

// Number
Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2; // true because both are 9007199254740992
Copy to Clipboard
You can use most operators to work with BigInts, including +, *, -, **, and % — the only forbidden one is >>>. A BigInt is not strictly equal to a Number with the same mathematical value, but it is loosely so.

BigInt values are neither always more precise nor always less precise than numbers, since BigInts cannot represent fractional numbers, but can represent big integers more accurately. Neither type entails the other, and they are not mutually substitutable. A TypeError is thrown if BigInt values are mixed with regular numbers in arithmetic expressions, or if they are implicitly converted to each other.

String type
The String type represents textual data and is encoded as a sequence of 16-bit unsigned integer values representing UTF-16 code units. Each element in the string occupies a position in the string. The first element is at index 0, the next at index 1, and so on. The length of a string is the number of UTF-16 code units in it, which may not correspond to the actual number of Unicode characters; see the String reference page for more details.

JavaScript strings are immutable. This means that once a string is created, it is not possible to modify it. String methods create new strings based on the content of the current string — for example:

A substring of the original using substring().
A concatenation of two strings using the concatenation operator (+) or concat().
Beware of "stringly-typing" your code!
It can be tempting to use strings to represent complex data. Doing this comes with short-term benefits:

It is easy to build complex strings with concatenation.
Strings are easy to debug (what you see printed is always what is in the string).
Strings are the common denominator of a lot of APIs (input fields, local storage values, XMLHttpRequest responses when using responseText, etc.) and it can be tempting to only work with strings.
With conventions, it is possible to represent any data structure in a string. This does not make it a good idea. For instance, with a separator, one could emulate a list (while a JavaScript array would be more suitable). Unfortunately, when the separator is used in one of the "list" elements, then, the list is broken. An escape character can be chosen, etc. All of this requires conventions and creates an unnecessary maintenance burden.

Use strings for textual data. When representing complex data, parse strings, and use the appropriate abstraction.
