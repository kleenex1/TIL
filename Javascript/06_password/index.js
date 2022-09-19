const passwordInput = document.querySelector('#input-password')

function password() {
  let p1 = document.querySelector('#password1').value;
  let p2 = document.querySelector('#password2').value;
    if( p1 != p2 ) {
      alert("비밀번호가 다릅니다.");
      return false;
    } else{
      alert("비밀번호가 일치합니다.");
      return true;
    }
}

passwordInput.addEventListener('click', password)