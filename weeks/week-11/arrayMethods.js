
print = console.log
// # Array Methods – תרגילים

// ---

// ## חלק א' – map / filter

// ---

// ### תרגיל 1

// יש מערך מספרים:


const arr1 = [1, 2, 3, 4, 5];

const arr1Multy = arr1.map((x) => x*2);
console.log(arr1Multy)


// ### תרגיל 2

// המר את כל המחרוזות לאותיות גדולות:


const arr2 = ["hello", "world"];
console.log(arr2.map((val) => val.toUpperCase()))

// ---

// <div dir="rtl">

// ### תרגיל 3

// יש מערך של מחירים. הוסף לכל מחיר מע"מ 17% באמצעות `map`.

const price = [50,34,56,78,90,100];
console.log(price.map((n) => Number((n * 1.17).toFixed(2))))


// ### תרגיל 4

// סנן רק מספרים זוגיים מתוך:


const numbrs = [1, 2, 3, 4, 5, 6];

console.log(numbrs.filter(n => n%2==0))


// ### תרגיל 5

// סנן מחרוזות שאורכן גדול מ-3:


const arr3 = ["hi", "hello", "cat", "javascript"]
print(arr3.filter(val => val.length > 3))





// ### תרגיל 6

// יש מערך משתמשים:


const arrUser = [{ name: "Avi", age: 17 }, { name: "Dana", age: 22 }];
print(arrUser.filter(user => user["age"] > 18))




// ### תרגיל 8

// שלב `filter` + `map`:

// סנן רק מחירים מעל 100 ואז החזר אותם עם תוספת של 10%.

const price1 =[100,101,103,89,567,32];
console.log(price1.filter(
    (p)=> p>100).map(
        (p) => (p*1.10).toFixed(2)))


// ## חלק ב' – reduce

// ---

// ### תרגיל 9




const arr4 = [10, 20, 30]
const sum1 = (arr4.reduce((a,b) => a+b,0));
console.log(sum1)



// חשב מכפלה של כל המספרים במערך.

const arr5 = [10, 20, 30]
const sum2 = (arr4.reduce((a,b) => a*b,1));
console.log(sum2)

// ### תרגיל 11

// יש מערך מילים:


const arr6 = ["a", "b", "c"]
const sum3 = (arr6.reduce((a,b) => a+b,""));
console.log(sum3)

// <div dir="rtl">

// חבר אותן למחרוזת אחת.

// ---

// ### תרגיל 12

// יש מערך משתמשים עם גילאים — חשב ממוצע גילאים.

const age = [2,3,6,10,30,22]
console.log(age.reduce((a,b) => (a+b),0) / age.length)

// ### תרגיל 13

// קבל מערך מספרים והחזר אובייקט:
const arr7 = [2,3,6,10,30,22]
console.log(arr7.reduce((ass, num) => {
    if(num%2===0){
        ass.even.push(num)
    } else {
        ass.odd.push(num)
    } return ass 

}, {even: [], odd: []}))

// </div>


// ---

// ## חלק ג' – find / some / every



// ### תרגיל 14

// מצא את המספר הראשון הגדול מ-50.
const arr8 = [1,56,34,89,45,100]
console.log(arr8.find((n) => n >50))
// ### תרגיל 15n

// מצא משתמש לפי `id` מתוך מערך אובייקטים.

const objek = [{id: 1, name: "aharon"}, {id: 2, name: "momo"}, {id: 3, name: "david"}]
let num = 1
console.log(objek.find(({id})=> id === num))
// ### תרגיל 16

// בדוק האם יש לפחות מספר אחד שלילי (`some`).

const arr10 = [1,4,6,7,9,1]
console.log(arr10.some((n) => n < 0 ))

// ### תרגיל 17

// בדוק האם כל המספרים חיוביים (`every`).



// ### תרגיל 18

// בדוק האם כל המשתמשים מעל גיל 18.

const users = [{name: "ari", age: 20},{name: "momo", age: 20}];
console.log(users.every(({age})=> age > 18 ))
// ## חלק ד' – includes / indexOf

// ---

// ### תרגיל 19

// בדוק האם `"apple"` קיים במערך.

// const arr11 = ["banana", "apple"]
// console.log(arr11.includes("apple"))

// ### תרגיל 20

// מצא את האינדקס של מספר מסוים במערך.

// const arr12 = [1,56,34,89,45,100]
// console.log(arr12.indexOf(56))

// ### תרגיל 21

// בדוק האם ערך קיים החל מאינדקס מסוים בלבד.

// const arr12 = [1,56,34,89,45,100]
// console.log(arr12.indexOf(56,2))

// ## חלק ה' – forEach (תופעות לוואי)

// const arr11 = ["banana", "apple"]
// arr11.forEach((v,i) => console.log(i,v))


// ### תרגיל 22

// הדפס את כל האיברים במערך עם האינדקס שלהם.

const arr11 = ["banana", "apple"]
console.log(arr11[arr11.indexOf("banana") ,arr11.indexOf("banana")]);




// ### תרגיל 23

// צור מערך חדש ידנית באמצעות `forEach` ו-`push`.


const arr12 = ["banana", "apple"]
const arr13 = []
arr11.forEach(a => arr13.push(a))
console.log(arr13)

// ## חלק ו' – sort / reverse

const months = ["Aarch", "Jan", "Feb", "Dec"]
console.log(months.sort())

// ### תרגיל 24

// מיין מערך מספרים בסדר **עולה**.
const arr14 = [3,5,78,90,34,65,89,1];
console.log(arr14.sort());


// ### תרגיל 25

// מיין מערך מספרים בסדר **יורד**.

const arr15 = [3,5,78,90,34,65,89,1];
console.log(arr15.sort((a,b) => b-a));

// ### תרגיל 26

// מיין מערך אובייקטים לפי מחיר.

objPrice = [{banana: 30, apple: 47}]


// ### תרגיל 27

// הפוך את סדר המערך.

// ---

// ## חלק ז' – slice / splice

// ---

// ### תרגיל 28

// קח תת-מערך מתוך אינדקס 2 עד 5 (לא כולל 5).

// ---

// ### תרגיל 29

// הסר 2 איברים החל מאינדקס 1.

// ---

// ### תרגיל 30

// הוסף איבר למערך באמצע באמצעות `splice`.

// ---

// ### תרגיל 31

// החלף איבר קיים באחר.

// ---

// ## חלק ח' – flat / flatMap

// ---

// ### תרגיל 32

// שטח מערך מקונן ברמה אחת.

// ---

// ### תרגיל 33

// שטח מערך מקונן עמוק לחלוטין.

// ---

// ### תרגיל 34

// קבל מערך משפטים והחזר מערך של כל המילים (`flatMap`).

// ---

// ## חלק ט' – Chaining

// ---

// ### תרגיל 35

// יש מערך מוצרים — בצע chain אחד:

// - סנן מוצרים במלאי
// - מיין לפי מחיר
// - החזר רק שמות

// ---

// ### תרגיל 36

// יש מערך מספרים — בצע chain אחד:

// - סנן רק זוגיים
// - הכפל ב-2
// - חשב סכום

// ---

// ### תרגיל 37

// יש מערך משתמשים — בצע chain אחד:

// - סנן מעל גיל 18
// - החזר רק שמות
// - הפוך למחרוזת אחת עם פסיקים

// ---

// ## תרגילי חשיבה

// ---

// ### תרגיל 38 – groupBy

// ממש `groupBy` באמצעות `reduce`.

// קלט:

// </div>

// ```javascript
// [{ type: "fruit" }, { type: "veg" }, { type: "fruit" }]
// ```

// <div dir="rtl">

// פלט:

// </div>

// ```javascript
// {
//   fruit: [...],
//   veg: [...]
// }
// ```

// ---

// <div dir="rtl">

// ### תרגיל 39 – כפילויות (ללא Set)

// מצא האם יש כפילויות במערך — **ללא שימוש ב-Set**.

// ---

// ### תרגיל 40 – האלמנט הנפוץ ביותר

// מצא את האלמנט שמופיע הכי הרבה פעמים.

// ---

// ## תרגיל מסכם (חובה)

// ### תרגיל 41 – מערכת מוצרים

// </div>

// ```javascript
// const products = [
//   { name: "Laptop", price: 800, inStock: true,  category: "tech"    },
//   { name: "Phone",  price: 400, inStock: false, category: "tech"    },
//   { name: "Shirt",  price: 50,  inStock: true,  category: "fashion" }
// ];
// ```

// <div dir="rtl">

// בצע הכל ב-chain אחד:

// 1. סנן רק מוצרים במלאי
// 2. סנן רק מוצרים מעל 100
// 3. מיין לפי מחיר
// 4. החזר רק שמות
// 5. חבר למחרוזת אחת