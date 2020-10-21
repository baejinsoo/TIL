var name =  'jinsoo';
var letter = 'klda hi sjfl '+name+' \n\
hi ienlka dklfjklasjfi\n\
e hi dkasdkfjli.f askfljlsdsfjklasd\
fjil, dsfjn dfjasdkfjlkasd';

console.log(letter);

// 줄바꿈 : \ (visual code  내에서 줄바꿈)
// \n (실질적으로 줄바꿈)

var letter = `klda hi sjfl ${name} \n\
hi ienlka dklfjklasjfi\n\ ${1+1}
e hi dkasdkfjli.f askfljlsdsfjklasd\
fjil, dsfjn dfjasdkfjlkasd`;
console.log(letter);
