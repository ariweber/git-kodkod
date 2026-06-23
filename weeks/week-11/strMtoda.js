// String Methods – תרגילים

// תרגיל 1
// מחרוזת: " hello world "

const hello = "    hello world  "

console.log(hello.trim())




// תרגיל 2
// מחרוזת: "user@gmail.com"

const enail = "user@gmail.com"

console.log(enail.includes("@"))

// פלט צפוי: true


// תרגיל 3
// מחרוזת: "javascript"

// משימה: המר את כל האותיות לגדולות.

// יש להשתמש ב: toUpperCase
const lange = "javascript";
console.log(lange.toUpperCase())
// פלט צפוי: "JAVASCRIPT"


// תרגיל 4
// מחרוזת: "HELLO WORLD"
const a = "HELLO WORLD";

console.log(a.toLowerCase())
// משימה: המר את כל האותיות לקטנות.


// יש להשתמש ב: toLowerCase

// פלט צפוי: "hello world"


// תרגיל 5
// מחרוזת: "שלום עולם"

let a1 = "hello world"
a1 = a1.replaceAll(" ", "").length
console.log(a1)

// משימה: החזר את מספר התווים במחרוזת.

// יש להשתמש ב: length

// פלט צפוי: 9


// תרגיל 6
// מחרוזת: "JavaScript"
const l = "JavaScript";
console.log(l.slice(0,4))
// משימה: החזר את 4 התווים הראשונים.

// יש להשתמש ב: slice

// פלט צפוי: "Java"


// תרגיל 7
// מחרוזת: "JavaScript"
l1 = "JavaScript"
console.log(l1.slice(-7,-1))
// משימה: החזר את 6 התווים האחרונים.

// יש להשתמש ב: slice

// פלט צפוי: "Script"


// תרגיל 8
// מחרוזת: "https://example.com"
const domine = "https://example.com";
console.log(domine.startsWith("https"))
// משימה: בדוק האם המחרוזת מתחילה ב-"https".

// יש להשתמש ב: startsWith

// פלט צפוי: true


// תרגיל 9
// מחרוזת: "mywebsite.org"
const domine1 =  "mywebsite.org"
console.log(domine1.endsWith(".com"))
// משימה: בדוק האם המחרוזת מסתיימת ב-".com".

// יש להשתמש ב: endsWith

// פלט צפוי: false


// תרגיל 10
// מחרוזת: "שלום עולם"
const a3 = "hello world"
console.log(a3.replace("hello", "hi"))
// משימה: החלף את המילה "שלום" ב-"היי".

// יש להשתמש ב: replace

// פלט צפוי: "היי עולם"


// תרגיל 11
// מחרוזת: "banana"
const frige = "banana";

console.log(frige.replaceAll("a", "o"))



// משימה: החלף את כל האותיות "a" ב-"o".

// יש להשתמש ב: replaceAll

// פלט צפוי: "bonono"


// תרגיל 12
// מחרוזת: "one two three"
str = "one two three"
console.log(str.split(" "))
// משימה: פצל למערך לפי רווחים.

// יש להשתמש ב: split

// פלט צפוי: ["one", "two", "three"]


// תרגיל 13
// מחרוזת: "apple,banana,grape"
const str1 = "apple,banana,grape";
console.log(str1.split(",").slice(0,2))
// משימה: פצל למערך והחזר רק 2 איברים ראשונים.

// יש להשתמש ב: split

// פלט צפוי: ["apple", "banana"]


// תרגיל 14
// מחרוזת: "banana"
const a4 = "banana";
console.log(a4.indexOf("a"))
// משימה: מצא את המיקום של האות הראשונה "a".

// יש להשתמש ב: indexOf

// פלט צפוי: 1


// תרגיל 15
// מחרוזת: "banana"
const a5 = "banana";
console.log(a5.lastIndexOf("a"))
// משימה: מצא את המיקום של האות האחרונה "a".

// יש להשתמש ב: lastIndexOf

// פלט צפוי: 5


// תרגיל 16
// מחרוזת: "7"
const str2 = "7";
console.log(str2.padStart(3,0))
// משימה: הפוך למחרוזת באורך 3 תווים עם אפסים משמאל.

// יש להשתמש ב: padStart

// פלט צפוי: "007"


// תרגיל 17
// מחרוזת: "hi"
const str4 = "hi"
console.log(str4.padEnd(5,"*"))
// משימה: השלם לאורך 5 תווים עם "*" מימין.

// יש להשתמש ב: padEnd
// פלט צפוי: "hi***"


// תרגיל 18
// מחרוזת: "ha"
const str5 = "*******"
console.log(str5.repeat(2))
// משימה: חזור על המחרוזת 3 פעמים.

// יש להשתמש ב: repeat

// פלט צפוי: "hahaha"


// תרגיל 19
// מחרוזת: "Hello"
const str6 = "Hello";
console.log(str6.at(-1))
// משימה: החזר את התו הראשון.

// יש להשתמש ב: charAt

// פלט צפוי: "H"


// תרגיל 20
// מחרוזת: "Hello"

// משימה: החזר את התו האחרון.

// יש להשתמש ב: at

// פלט צפוי: "o"


// תרגיל 21
// מחרוזות: "שלום" ו-"עולם"
const lst1 = ["Hello", "world"]
console.log(lst1.join(" "))
// משימה: חבר ביניהן עם רווח באמצע.

// יש להשתמש ב: concat

// פלט צפוי: "שלום עולם"


// תרגיל 22
// מחרוזת: "JavaScript"
const str7 = "JavaScript"
console.log(str7.substring(2,6))
// משימה: החזר תת-מחרוזת מאינדקס 2 עד 6 (לא כולל 6).

// יש להשתמש ב: substring

// פלט צפוי: "vaSc"


// תרגיל 23
// מחרוזת: "AdminPanel"
const str8 = "AdminPanel";
console.log(str8.toLowerCase().includes("admin"))
// משימה: בדוק האם מכילה "admin" ללא תלות ברישיות.

// יש להשתמש ב: toLowerCase, includes

// פלט צפוי: true


// תרגיל 24
// מחרוזת: " hello"
const str9 =  " hello"
console.log(str9.trimStart())
// משימה: הסר רווחים רק מהתחלה.

// יש להשתמש ב: trimStart

// פלט צפוי: "hello"


// תרגיל 25
// מחרוזת: "hello "
const str10 = "   hello "
console.log(str10.trimEnd())
// משימה: הסר רווחים רק מהסוף.

// יש להשתמש ב: trimEnd

// פלט צפוי: "hello"

