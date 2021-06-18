
// // Wrapper Area
// const wrapper__Area = document.querySelector('#wrapper_Area');


// // Password And Confirm Password Fileds
// const passwordField = document.querySelector('#signUpPassword');
// const confirmPassword = document.querySelector('#signUpConfirmPassword');

// // Show Hide Password Element
// const showHidePassDom = Array.from(document.querySelectorAll('.showHide__Icon i'));

// // Pattrens Regex
// const patterns = { // All This Regex Code Is For Demo You Can Add Your Own Regex Code :)
//   username: /^[a-z]+\d?/,
//   email: /^[^\W\d\.-_]+\w\d?@[a-z0-9]+\.([a-z0-9]{2,6})(\.[a-z0-9]{2,6})?$/,
//   password: /^[^\d\W]\w+\d?\W?\w?/i,
// };

// // Aside Area
// const aside__Area = document.querySelector('#aside_Area');

// // Aside Sing-Up & Sign In Buttons
// const aside__SignUp_Button = document.querySelector('#aside_signUp_Btn');
// const aside__SignIn_Button = document.querySelector('#aside_signIn_Btn');

// // Every Time Click On Aside Sign-Up & Sing-In Buttons. Call Function Chnage Form Mode
// aside__Area.addEventListener('click', chnageFormMode);
// aside__Area.addEventListener('click', chnageFormMode);

// // - - - - -  Functions - - - - - //

// // Change Form Mode Function
// function chnageFormMode(e) {
//   // Check. If The Target Element Is Aside Sign-Up Button
//   if(e.target === aside__SignUp_Button){
//     // Add Class [ Sign Up Mode Active ] On Wrapper Area
//     wrapper__Area.classList.add('sign-up__Mode-active');
//   };
//   // Check. If The Target Element Is Aside Sign-In Button
//   if(e.target === aside__SignIn_Button){
//     // Remove Class [ Sign Up Mode Active ] From Wrapper Area
//     wrapper__Area.classList.remove('sign-up__Mode-active');
//   };
// };

// // Function Show Hide Password
// (function showHidePass() {
//   // Loop On All The Show Hide Password Icon
//   showHidePassDom.forEach(icon =>{
//     // When Click On Any Show Hide Icon...
//     icon.addEventListener('click', () => {
//       // Select The Target Password Input
//       const targetAreaInput = icon.parentElement.parentElement.querySelector('.field input');
//       // If The Target Icon Has Hide-icon
//       if(icon.className === 'bx bx-hide'){
//         // Change The Target Icon Class
//         icon.className = 'bx bx-show';
//         // Change The Target Input Area Type
//         targetAreaInput.setAttribute('type', 'text');
//       }else{ // else
//         // Change The Target Icon Class
//         icon.className = 'bx bx-hide';
//         // Change The Target Input Area Type
//         targetAreaInput.setAttribute('type', 'password');
//       };
//     });
//   });
// })();

