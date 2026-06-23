const print = console.log()
print
// # Functions & Scope 2 – תרגילים

// ---

// ## תרגילים בסיסיים

// ---

// ### תרגיל 1

// כתוב פונקציה שמקבלת מספר ומחזירה את המספר **כפול 3**.
function multy3(n){
    return n*3
}


// ### תרגיל 2

// כתוב פונקציה שמקבלת מחרוזת ומחזירה את **האורך** שלה.
function lenStr(myStr){
    return myStr.length
}
console.log(lenStr([1,2,3,4,5,6,7,8]))
// ---

// ### תרגיל 3

// כתוב פונקציה שמקבלת מספר ומחזירה אם הוא **חיובי / שלילי / אפס**.

function check(n){
    if (n > 0){
        return ("positiv")
    } else if (n<0){
        return ("negativ")
    } else if (n===0){
        return ("0")
    }
   
    
}

console.log(check(-0))
// ### תרגיל 4

// כתוב פונקציה שמקבלת שני מספרים ומחזירה את **הגדול** מביניהם.

function bigNum(a,b){
    return a > b? a : b
}
console.log(bigNum(2,-3))

// ### תרגיל 5

// כתוב פונקציה שמקבלת מערך ומחזירה את **מספר האיברים** בו.
// function lenStr(mylist){
//     return myStr.length
// }



// ## תרגילים – Scope והבנה

// ---

// ### תרגיל 6

// מה יודפס? הסבר למה.


let a = 3;

function test() {
  a = 7;
}

test();
console.log(a);


// ### תרגיל 7

// מה יודפס? למה מתקבלת תוצאה כזו?

// </div>

// ```javascript
function test() {
  let a = 5;
}

test();
console.log(a);
// כי הגלובלי לא מכיר משתנה פנימי 

// ---

// <div dir="rtl">

// ### תרגיל 8

// מצא את הבעיה בקוד. האם זה באג או קוד תקין? הסבר.




let x = 10;

function change() {
  let x = 20;
}

console.log(x);


// ---

// <div dir="rtl">

// ### תרגיל 9

// מה יודפס?

// </div>

// ```javascript
// let num = 1;

// function first() {
//   num++;
// }

// function second() {
//   num = num + 2;
// }

// first();
// second();

// console.log(num);
// ```

// ---

// <div dir="rtl">

// ### תרגיל 10

// תקן את הקוד כך שהמשתנה **לא יהיה גלובלי**.

// </div>

// ```javascript
// let message = "Hi";

// function print() {
//   console.log(message);
// }
// ```

// ---

// <div dir="rtl">

// ## תרגילים בינוניים

// ---

// ### תרגיל 11

// כתוב פונקציה שמקבלת מערך ומחזירה את **המספר הקטן ביותר** בו.

// ---

// ### תרגיל 12

// כתוב פונקציה שמקבלת שני מספרים ומחזירה `true` אם הראשון **מתחלק** בשני.

// ---

// ### תרגיל 13

// כתוב פונקציה שמקבלת מערך של מחרוזות ומחזירה **מחרוזת אחת מחוברת** (join).

// ---

// ### תרגיל 14

// מה יודפס?

// </div>

// ```javascript
// let x = 5;

// function test(x) {
//   x = x + 10;
//   return x;
// }

// let result = test(x);
// console.log(x);
// console.log(result);
// ```

// ---

// <div dir="rtl">

// ### תרגיל 15

// כתוב פונקציה שמקבלת מספר `n` ומדפיסה את כל המספרים מ-1 עד `n` — **בלי להשתמש במשתנה גלובלי**.

// ---

// ## תרגילים מתקדמים

// ---

// ### תרגיל 16

// כתוב פונקציה שמקבלת מערך ומחזירה **מערך חדש ללא כפילויות**.

// ---

// ### תרגיל 17

// מצא את הבאג:

// </div>

// ```javascript
// let sum = 0;

// function add(numbers) {
//   for (let i = 0; i < numbers.length; i++) {
//     sum += numbers[i];
//   }
// }

// add([1, 2]);
// add([3, 4]);

// console.log(sum);
// ```

// <div dir="rtl">

// - למה זה בעייתי?
// - איך מתקנים?

// ---

// ### תרגיל 18

// כתוב פונקציה שמקבלת מערך ומחזירה את **סכום האיברים הזוגיים** בלבד.

// ---

// ### תרגיל 19

// מה יודפס?

// </div>

// ```javascript
// let x = 1;

// function a() {
//   let x = 2;

//   function b() {
//     console.log(x);
//   }

//   b();
// }

// a();
// ```

// ---

// <div dir="rtl">

// ### תרגיל 20

// שפר את הקוד כך שלא תהיה תלות חיצונית:

// </div>

// ```javascript
// let discount = 0.1;

// function getPrice(price) {
//   return price - price * discount;
// }
// ```

// <div dir="rtl">

// - הפוך את הפונקציה ליותר גנרית
// - בלי שימוש במשתנה גלובלי

// </div>