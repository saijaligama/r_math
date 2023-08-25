/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


function convertform(form){
    var firstvalue = 0;
    for (var i = 0; i <= form.count-1; i++) {
       // Find first non-blank entry
       if (form.elements[i].value != null && form.elements[i].value.length != 0) {
	  if (i == 0 && form.elements[1].value != "") return false;
	  firstvalue = form.elements[i].value / form.elements[i].factor;
	  break;
       }
    }
    if (firstvalue == 0) {
       clearform(form);
       return false;
    }
    for (var i = 0; i <= form.count-1; i++)
       form.elements[i].value = formatvalue((firstvalue * form.elements[i].factor), form.rsize);
    return true;
}

function formatvalue(input, rsize) {
   var invalid = "**************************";
   var nines = "999999999999999999999999";
   var strin = "" + input;
   var fltin = parseFloat(strin);
   if (strin.length <= rsize) return strin;
   if (strin.indexOf("e") != -1 ||
       fltin > parseFloat(nines.substring(0,rsize)+".4"))
      return invalid.substring(0, rsize);
   var rounded = "" + (fltin + (fltin - parseFloat(strin.substring(0, rsize))));
   return rounded.substring(0, rsize);
}

// truncate a scientific number to si decimal digits
function trunc(input, si) {
    //si = 3;
    var strin = "" + input;
    //alert(strin);
    var epos = strin.indexOf("e"), endpos = strin.length;
    
    var str1 = strin.substring(0, si+1)+strin.substring(epos, endpos);
    //alert(str1);
    if ( epos != -1) return str1;
    else return input;
}

function clearform(form) {
    for (var i = 0; i <= form.count-1; i++) form.elements[i].value = "";
    return true;
}


function convertTemp(form) {
	if (form.elements[0].value != null && form.elements[0].value.length != 0)
		form.elements[1].value = 32+1.8*form.elements[0].value;
	else form.elements[0].value = (form.elements[1].value-32)/1.8;	
}

// --------------------------Arithmetic---------------------------------------
var op = "";
function calc(form) {
	//alert("Op is"+op);
        var a = form.elements[0].value, b = form.elements[4].value, r=8;
	if ( a=="" || b=="") 
            alert("Fill the first two boxes first please.");
	switch (op)
	{
	case '+':
	  form.elements[r].value=parseFloat(a)+parseFloat(b);
          // pay special attention to + because it concatenante as string so parseFloat or use 1.0*a+1.0*b
	  break;
	  
	case '-':
	  form.elements[r].value=a-b;
	  break;
	  
	case '*':
	  form.elements[r].value=a * b;
	  break;
	  
	case '/':
	  form.elements[r].value=a / b;
	  break;
	  
	case '%':
	  form.elements[r].value=a % b;
	  break;
	 
	case '^':
	  form.elements[r].value= Math.pow(a , b);
	  break;
	  
	}	
}

function change(form) {
	if ( form.elements[2].value=="" && form.elements[5].value=="") {
		if ( op == '+' ) form.elements[2].value = form.elements[0].value * (1+form.elements[3].value/100);
		else form.elements[2].value = form.elements[0].value * (1-form.elements[3].value/100);
		form.elements[5].value = form.elements[0].value * form.elements[3].value/100;}
		
	else if ( form.elements[0].value=="" && form.elements[3].value=="") {
		if ( op == '+' ) form.elements[0].value = form.elements[2].value - form.elements[5].value;
		else form.elements[0].value = parseFloat(form.elements[2].value) + parseFloat(form.elements[5].value);
		form.elements[3].value = form.elements[5].value / form.elements[0].value*100;}
		
	else if ( form.elements[0].value=="" && form.elements[2].value=="") {
		form.elements[0].value = form.elements[5].value / form.elements[3].value*100;
		if ( op == '+' ) form.elements[2].value = parseFloat(form.elements[0].value) + parseFloat(form.elements[5].value);
		else form.elements[2].value = form.elements[0].value - form.elements[5].value;}
		
	else if ( form.elements[3].value=="" && form.elements[5].value=="") {
		if ( op == '+' ) form.elements[5].value = form.elements[2].value - form.elements[0].value;
		else form.elements[5].value = form.elements[0].value - form.elements[2].value;
		form.elements[3].value = form.elements[5].value / form.elements[0].value*100;}	
	
	else if ( form.elements[2].value=="" && form.elements[3].value=="") {
		if ( op == '+' ) form.elements[2].value = parseFloat(form.elements[0].value) + parseFloat(form.elements[5].value);
		else form.elements[2].value = form.elements[0].value - form.elements[5].value;
		form.elements[3].value = form.elements[5].value / form.elements[0].value*100;}	
		
	else if ( form.elements[0].value=="" && form.elements[5].value=="") {
		if ( op == '+' ) form.elements[0].value = form.elements[2].value / (1 + form.elements[3].value*0.01);
		else form.elements[0].value = form.elements[2].value / (1 - form.elements[3].value*0.01);
		form.elements[5].value = form.elements[3].value*0.01 * form.elements[0].value;}		
}

function rate(form) {
	if ( form.elements[0].value=="" ) form.elements[0].value = form.elements[1].value *form.elements[2].value / form.elements[3].value;	
	else if ( form.elements[1].value=="" ) form.elements[1].value = form.elements[0].value *form.elements[3].value / form.elements[2].value;	
	else if ( form.elements[2].value=="" ) form.elements[2].value = form.elements[0].value *form.elements[3].value / form.elements[1].value;
	else if ( form.elements[3].value=="" ) form.elements[3].value = form.elements[1].value *form.elements[2].value / form.elements[0].value;		
}

//------------------------- Scientific ----------------------------
function calFun(form) {
	var j=22, krad=1, tmp=form.elements[0].value;
	if (form.elements[0].value=="" && op != 'e' && op != 'pi' ) 
            alert("Fill the first box, then click the function please.");
	//alert(trunc(1.23456789e-16, 5));
	switch (op)
	{
	case 'n!':
		for (x=1, i=2; i<= form.elements[0].value; i++) x*= i;
	  form.elements[j].value=x;
	  break;
	  
	case '2n':
	  form.elements[j].value=Math.pow(2,form.elements[0].value);
	  break;
	  
	case 'x2':
	  form.elements[j].value=form.elements[0].value*form.elements[0].value;
	  break;
	  
	case 'x3':
	  form.elements[j].value=form.elements[0].value*form.elements[0].value*form.elements[0].value;
	  break;
	  
	case 'xr2':
	  form.elements[j].value=Math.pow(form.elements[0].value, 1/2);
	  break;
	 
	case 'xr3':
	  form.elements[j].value=Math.pow(form.elements[0].value, 1/3);
	  break;
	
	// ------------------------  
	case '1/x':
		form.elements[j].value=1/form.elements[0].value;
	  	break;
	
	case 'ex':
	  form.elements[j].value=Math.pow(Math.E,form.elements[0].value);
	  break;
	  
	case 'log':
		form.elements[j].value=Math.log(form.elements[0].value)/Math.log(10);
		break;
		
	case 'ln':
		form.elements[j].value=Math.log(form.elements[0].value);
		break;	
	
	case 'deg':
		form.elements[j].value=180*form.elements[0].value/Math.PI;
		break;	
	
	case 'rad':
		form.elements[j].value=Math.PI*form.elements[0].value/180;
		break;
	
	case 'sin':
		
		if (form.elements[krad].checked) form.elements[j].value=Math.sin((Math.PI)/180*form.elements[0].value);
		else form.elements[j].value=Math.sin(tmp);
		break;
	
	case 'cos':
		if (form.elements[krad].checked) form.elements[j].value=Math.cos(Math.PI*form.elements[0].value/180);
		else form.elements[j].value=Math.cos(tmp);
		break;
			
	case 'tan':
		if (form.elements[krad].checked) form.elements[j].value=Math.tan(Math.PI*form.elements[0].value/180);
		else form.elements[j].value=Math.tan(tmp);
		break;
	
	case 'asin':
                if (form.elements[krad].checked) 
                    form.elements[j].value = Math.asin(form.elements[0].value)*180/Math.PI;
		else form.elements[j].value =Math.asin(form.elements[0].value);
		break;
	
	case 'acos':
		if (form.elements[krad].checked) 
                    form.elements[j].value = Math.acos(form.elements[0].value)*180/Math.PI;
		else form.elements[j].value =Math.acos(form.elements[0].value);
		break;
			
	case 'atan':
		if (form.elements[krad].checked) 
                    form.elements[j].value = Math.atan(form.elements[0].value)*180/Math.PI;
		else form.elements[j].value =Math.atan(form.elements[0].value);
		break;
	
	case 'e':
		form.elements[0].value=Math.E;
		break
	
	case 'pi':
		form.elements[0].value=Math.PI;
		break	
	}
        
        //clean up
        form.elements[j].value = trunc(form.elements[j].value, 4);
        
	
}

function clear1st(form) {
	form.elements[0].value = "";	
}
function clear2nd(form) {
	form.elements[7].value = "";	
}
function clear(form, i) {
	form.elements[i].value = "";	
}

function clear056(form) {
    form.elements[0].value = "";
    form.elements[5].value = "";
    form.elements[6].value = "";
}

// ------------------------- STAT --------------------------------
function sorted(form) {
	
        if (form.elements[0].value == "") 
            alert("Please fill in the empty big box with numbers");
        var str = form.elements[0].value;
        var br  = str.split(/\s+/);
        if ( br[br.length-1] =="") br.pop();
        br.sort(function(a,b){return a-b;});
        for (i=0; i<br.length; i++) br[i] = parseFloat(br[i]);
        form.elements[0].value = "";
        for (i=0; i<br.length; i++) form.elements[0].value += br[i]+" ";  
}

// ------  float array ar is filled in stat form- - - -
function fillStat(br, form) {
    var kout = 5;
    var count=br.length, sum2=0, diff2=0, avg, i;
    br.sort(function(a,b){return a-b;});
    for (i=0; i<count; i++) sum2 += br[i]; 
    avg = sum2/count; 
    //alert("count="+count+"avg="+avg);
    form.elements[kout].value = br[0];	// min 
     form.elements[kout+1].value = br[Math.floor(count/4)];   // 1st Quantile
     if (count %2 == 1) form.elements[kout+2].value = br[Math.floor(count/2)];
     else form.elements[kout+2].value = 0.5*(br[count/2]+br[count/2 -1]);  // median
     form.elements[kout+3].value = br[Math.floor(count*3/4)];   // 3rd Quantile
     form.elements[kout+4].value = br[count-1]; // max

     // compute mode
     var len = 1, maxlen = 0, leni = 0;
     for (i =0; i<count; i++ ) {
             diff2 += (br[i]-avg)*(br[i]-avg);
             if (br[i] == br[i+1] ) len++;
             else {
                     if (len>maxlen) {maxlen = len; leni=i;}
                     len =1; 
             }
     }
     
     form.elements[kout+5].value = sum2; // sum
     form.elements[kout+6].value = count;  // count
     form.elements[kout+7].value = avg;  // avg
     form.elements[kout+8].value = br[leni];  // mode
     form.elements[kout+9].value = Math.sqrt(diff2/(count-1)); // dev
 }
    

function stat(form) {
	var kw = 3, sum =0, wsum=0, i;
        
        if ( form.elements[0].value == "") {
            alert("Please enter numbers seperated by space into the big box");
        }
        else {
            // alert("text area is "+form.elements[0].value);
            var br = form.elements[0].value.split(/\s+/);
           if ( br[br.length-1] =="") br.pop();
            for (i=0; i<br.length; i++) br[i] = parseFloat(br[i]); 
            
            // for weighted avg
            if (form.elements[kw].checked) {
		sum=0; wsum=0;
                for (i=0; i<br.length; i=i+2) {
                    sum += br[i]*br[i+1];
                    wsum += br[i+1];
                }
                form.elements[kw+1].value = sum/wsum;
            }
            
            else     fillStat(br, form);
            
        }		
}

function factorial(n) {
	for (var x=1, i=2; i<= n; i++) x*= i;
	//alert("n="+n+", x="+x);
	return x;
}

function comb(form) {
	var kout = 15;
	form.elements[kout+4].value = factorial(form.elements[kout].value)/
		factorial(form.elements[kout].value-form.elements[kout+1].value);
	form.elements[kout+3].value = form.elements[kout+4].value/
		factorial(form.elements[kout+1].value);
}

// -----------------------------------------------Financial-------------------------------
function invest(form) {
    var pv = form.elements[0].value,
        n = form.elements[1].value,
        r = form.elements[2].value,
        fv = form.elements[3].value;
    if (pv == "") form.elements[0].value = fv/Math.pow(1+r*0.01,n);
    else if (n == "") form.elements[1].value = Math.log(fv/pv)/Math.log(1+r*0.01);
    else if (r == "") form.elements[2].value = 100*(Math.pow(fv/pv, 1/n)-1);
    else if (fv == "") form.elements[3].value = pv*Math.pow(1+r*0.01,n);        
}

function retire(form) {
    var pv = form.elements[0].value,
        av = form.elements[1].value,
        n = form.elements[2].value,
        r = form.elements[3].value*0.01;
    form.elements[4].value = pv*Math.pow(1+r,n)+av*(Math.pow(1+r,n)-1)*(1+r)/r;        
}

function loan(form) {
    var b = form.elements[0].value,
        c = form.elements[1].value,
        d = form.elements[2].value/1200, x=Math.pow(1+d, c),
        f = form.elements[3].value, y=Math.pow(1+d, f);
    form.elements[4].value = x*d*b/(x-1); // PMT
    var e = form.elements[4].value;
    form.elements[5].value = f*e - (y-1)/(x-1)*b; // total interest
    form.elements[6].value = f*e - form.elements[5].value; // total principle
    form.elements[7].value = form.elements[0].value - form.elements[6].value;
}   

function balloon(form) {
    var m = form.elements[0].value,
        r1 = form.elements[1].value, r = r1/1200,
        k  = form.elements[2].value, y=Math.pow(1+r, k);
        
    var L = form.elements[3].value; // loan amount
    var x = form.elements[4].value; // monthly payment
    var bal = form.elements[5].value; // loan balance, last one is balloon amount
    
    if (bal == "") form.elements[5].value = (L-x/r)*y+x/r;
    else if (L == "")  {form.elements[3].value = (bal-x/r)/y+x/r; L = form.elements[3].value;}
    else if (x == "")  {form.elements[4].value = (L*y-bal)*r/(y-1); x = form.elements[4].value;}
    //alert("L= "+L+"y= "+y+"r= "+r);
    form.elements[6].value = 1*x + (L*r-x)*Math.pow(1+r, k-1); // interest paid in that month
    form.elements[7].value = (L*r-x)*(y-1)/r+k*x; // total interest paid so far
}   

// -----------------------------------------------Unit-------------------------------

function today(form) {
    var wk = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
    var today = new Date();
    form.elements[1].value = today.getFullYear();
    form.elements[2].value = today.getMonth()+parseInt(1);
    form.elements[3].value = today.getDate();
    form.elements[4].value = wk[today.getDay()];
}

function timediff(form) {
    var wk = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
    var a1 = form.elements[1].value,
        a2 = form.elements[2].value,
        a3 = form.elements[3].value,
        a7 = form.elements[7].value,
        a8 = form.elements[8].value,
        a9 = form.elements[9].value;
        if (a7 == "") a7 =0;
        if (a8 == "") a8 = 0;
        if (a9 == "") a9 = 0;

    var day1 = new Date(), day2 = new Date(), day3 = new Date();
    day1.setFullYear(a1,a2-1,a3);
    day2.setFullYear(a7,a8-1,a9);
    form.elements[4].value = wk[day1.getDay()];
    
    if ( op == '+') 
    day3.setFullYear(parseInt(a1)+parseInt(a7), a2-1+parseInt(a8), parseInt(a3)+parseInt(a9));
    else if (day1 > day2) day3.setFullYear(a1-a7, a2-1-a8, a3-a9);
    else day3.setFullYear(a7-a1, a8-1-a2, a9-a3);
    
    form.elements[10].value = day3.getFullYear();
    form.elements[11].value = day3.getMonth()+parseInt(1)
    form.elements[12].value = day3.getDate();
    form.elements[13].value = wk[day3.getDay()];
    
    // if the duration is less than 1000 years, the last box is the #days difference
    if (parseInt(form.elements[10].value) < 1000) {
        form.elements[13].value = 
                Math.abs(Math.floor( (day2.getTime() - day1.getTime())/(1000*24*3600) ))+" days";
    }
        
    
}

function now(form) {
    var today = new Date();
    form.elements[2].value = today.getHours();
    form.elements[3].value = today.getMinutes();
    form.elements[4].value = today.getSeconds();
}

// convert time k (1, 2) from am/pm to 24 hour time
function to24(form,k) {
    if ( k == 2) k = 9; else k = 2;
    if (form.elements[k].value =="") form.elements[k].value =0;
    var hr = parseInt(form.elements[k].value);
    if (hr == 12 && form.elements[k+3].checked) return hr-12;
    if (hr != 12 && form.elements[k+4].checked) return hr+12;
    return hr;
}

// write box 13, 16, 17
function toam(form, hour) {
    form.elements[17].checked = false;
    form.elements[18].checked = false;
    if (hour>12) {
        form.elements[14].value = hour-12;
        form.elements[18].checked = true;
    }
    else if ( parseInt(hour) <1 ) {
        form.elements[14].value = parseInt(hour)+parseInt(12);
        form.elements[17].checked = true;
    }
    else if (hour == 12) {
        form.elements[14].value = hour;
        form.elements[18].checked = true;
    }
    else {
        form.elements[14].value = hour;
        form.elements[17].checked = true;
    }
}

function timecal(form) {
    var a3 = form.elements[3].value,
        a4 = form.elements[4].value,
        a10 = form.elements[10].value,
        a11 = form.elements[11].value;
        if (a10 == "") a10 =0;
        if (a11 == "") a11 = 0;
        if (a4 == "") a4 = 0;
        if (a3 == "") a3 = 0;

    var day1 = new Date(), day2 = new Date(), day3 = new Date();
    var h1 = to24(form, 1), h2 = to24(form, 2);
    
    day1.setHours(h1); day1.setMinutes(a3); day1.setSeconds(a4);
    day2.setHours(h2); day2.setMinutes(a10); day2.setSeconds(a11);
    
    if ( op == 'Dur') {
        if (day1 > day2) {
            day3.setHours(h1-h2);
            day3.setMinutes(a3-a10); 
            day3.setSeconds(a4-a11);
        }
        else {
            day3.setHours(h2-h1);
            day3.setMinutes(a10-a3); 
            day3.setSeconds(a11-a4);
        }
    }
    
    else if ( op == '+') {
        day3.setHours(parseInt(h1)+parseInt(h2));
        day3.setMinutes(parseInt(a3)+parseInt(a10));
        day3.setSeconds(parseInt(a4)+parseInt(a11));
    }  
    
    else {
        day3.setHours(h1-h2);
        day3.setMinutes(a3-a10); 
        day3.setSeconds(a4-a11);
    }
    
    if (op == 'Dur') form.elements[14].value = day3.getHours();
    else  toam(form, day3.getHours());
    form.elements[15].value = day3.getMinutes();
    form.elements[16].value = day3.getSeconds();
    
}
