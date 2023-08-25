/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

// --------------------------------------geometry---------------------------------------------
function eqside(form) {
    if (form.elements[0].value !="") {
        switch (op)
	{
	case '3':
            form.elements[5].value = 3*form.elements[0].value;
            form.elements[6].value = 0.4330127*form.elements[0].value*form.elements[0].value;
            break;
        case '4':
            form.elements[5].value = 4*form.elements[0].value;
            form.elements[6].value = form.elements[0].value*form.elements[0].value;
            break;
        case '5':
            form.elements[5].value = 5*form.elements[0].value;
            form.elements[6].value = 1.72048*form.elements[0].value*form.elements[0].value;
            break;
        case '6':
            form.elements[5].value = 3*form.elements[0].value;
            form.elements[6].value = 2.59808*form.elements[0].value*form.elements[0].value;
            break;
        }
    } 
    else if (form.elements[5].value !="") {
        switch (op)
	{
	case '3':
            form.elements[0].value = form.elements[5].value/3;
            form.elements[6].value = 0.4330127*form.elements[0].value*form.elements[0].value;
            break;
        case '4':
            form.elements[0].value = form.elements[5].value/4;
            form.elements[6].value = form.elements[0].value*form.elements[0].value;
            break;
        case '5':
            form.elements[0].value = form.elements[5].value/5;
            form.elements[6].value = 1.72048*form.elements[0].value*form.elements[0].value;
            break;
        case '6':
            form.elements[0].value = form.elements[5].value/6;
            form.elements[6].value = 2.59808*form.elements[0].value*form.elements[0].value;
            break;
        }
    } 
    if (form.elements[6].value !="") {
        switch (op)
	{
	case '3':
            form.elements[0].value = Math.sqrt(form.elements[6].value/0.4330127);
            form.elements[5].value = 3*form.elements[0].value;
            break;
        case '4':
            form.elements[0].value = Math.sqrt(form.elements[6].value);
            form.elements[5].value = 4*form.elements[0].value;
            break;
        case '5':
            form.elements[0].value = Math.sqrt(form.elements[6].value/1.72048);
            form.elements[5].value = 5*form.elements[0].value;
            break;
        case '6':
            form.elements[0].value = Math.sqrt(form.elements[6].value/2.59808);
            form.elements[5].value = 6*form.elements[0].value;
            break;    
        }
    } 
}

function isocles(form) {
    var a = form.elements[0].value, h = form.elements[1].value;
    form.elements[3].value = 2*Math.sqrt(h*h+a*a/4)+parseFloat(a);
    form.elements[4].value = a*h/2;
}

function rect(form) {
    var a = form.elements[0].value, h = form.elements[1].value;
    form.elements[3].value = 2*h+2*parseFloat(a);
    form.elements[4].value = a*h;
}


function rtri(form) {
    if ( op == 'R.Triangle') {
        if ( form.elements[0].value =="") 
            form.elements[0].value = Math.sqrt(form.elements[2].value *form.elements[2].value 
                - form.elements[1].value *form.elements[1].value  );
        else if ( form.elements[1].value =="") 
            form.elements[1].value = Math.sqrt(form.elements[2].value *form.elements[2].value 
                - form.elements[0].value *form.elements[0].value  );
        else form.elements[2].value = Math.sqrt(form.elements[1].value *form.elements[1].value 
                + form.elements[0].value *form.elements[0].value  );
        form.elements[3].value = parseFloat(form.elements[2].value) + parseFloat(form.elements[1].value)
                + parseFloat(form.elements[0].value);
        form.elements[4].value = parseFloat(form.elements[0].value) * form.elements[1].value/2;
    }
    else {
        var a = parseFloat(form.elements[0].value),
            b = parseFloat(form.elements[1].value),
            c = parseFloat(form.elements[2].value),
            s = (a+b+c)/2;
            //alert("s="+s);
        form.elements[3].value = 2*s;
        form.elements[4].value = Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }
}

function isotrape(form) {
    var a = form.elements[0].value, 
        b = form.elements[1].value,
        h = form.elements[2].value,
        s = form.elements[3].value;
     //alert('a='+a+", b="+b+", h="+h+", s="+s);  
    if ( a=="" )  {
        a = b - 2*Math.sqrt(s*s-h*h);
        form.elements[0].value = a;
    }  
    else if ( b=="" )  {
        b = parseFloat(a) + 2*Math.sqrt(s*s-h*h);
        form.elements[1].value = b;
    }
    else if ( h=="" )  {
        h = Math.sqrt(s*s-(b-a)*(b-a)/4);
        form.elements[2].value = h;
    }
    else if (s=="")  {
        s = Math.sqrt(parseFloat(h*h)+(b-a)*(b-a)/4);
        form.elements[3].value = s;
    }
    //alert('a='+a+", b="+b+", h="+h+", s="+s);
    form.elements[5].value = 2*s+parseFloat(a)+parseFloat(b);
    form.elements[6].value = (parseFloat(a)+parseFloat(b))*h/2;
}

function rtrape(form) {
    var a = form.elements[0].value, 
        b = form.elements[1].value,
        h = form.elements[2].value,
        s = form.elements[3].value;
    //alert('a='+a+", b="+b+", h="+h+", s="+s);  
    if ( a=="" )  {
        a = b - Math.sqrt(s*s-h*h);
        form.elements[0].value = a;
    }  
    else if ( b=="" )  {
        b = parseFloat(a) + Math.sqrt(s*s-h*h);
        form.elements[1].value = b;
    }
    else if ( h=="" )  {
        h = Math.sqrt(s*s-(b-a)*(b-a));
        form.elements[2].value = h;
    }
    else if (s=="")  {
        s = Math.sqrt(parseFloat(h*h)+(b-a)*(b-a));
        form.elements[3].value = s;
    }
    //alert('a='+a+", b="+b+", h="+h+", s="+s);
    form.elements[5].value = parseFloat(h)+parseFloat(s)+parseFloat(a)+parseFloat(b);
    form.elements[6].value = (parseFloat(a)+parseFloat(b))*h/2;
    form.elements[8].value = Math.PI*(parseFloat(a*a)+parseFloat(b*b))+ Math.PI*(parseFloat(a)+parseFloat(b))*s;
    form.elements[9].value = Math.PI*(parseFloat(a*a)+parseFloat(a*b)+parseFloat(b*b))*h/3; //frustum volume
}

function parallel(form) {
    var b = form.elements[0].value, 
        h = form.elements[1].value,    
        a = form.elements[2].value;
    form.elements[4].value = parseFloat(2*b)+parseFloat(2*a); // circum
    form.elements[5].value = b*h; // area
}

function rhombus(form) {
    var a = form.elements[0].value, 
        h = form.elements[1].value,
        p = form.elements[2].value,
        q = form.elements[3].value,
        S = form.elements[4].value, r, C;
     //alert('a='+a+", b="+b+", h="+h+", s="+s);  
    if ( a !="" && p !="" )  {
        q = Math.sqrt(4*a*a-p*p);  form.elements[3].value = q;
        h = p*q/(2*a); form.elements[1].value = h;
        S = a*h; form.elements[4].value = S;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }  
    else if ( a !="" && q !="" )  {
        p = Math.sqrt(4*a*a-q*q);  form.elements[2].value = p;
        h = p*q/(2*a); form.elements[1].value = h;
        S = a*h; form.elements[4].value = S;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( a !="" && h !="" )  {
        S = a*h; form.elements[4].value = S;
        var aa = a*a,  
                rp = Math.sqrt(parseFloat(aa)+parseFloat(S) ),
                rm = Math.sqrt(parseFloat(aa)-parseFloat(S) );
        p = parseFloat(rp)+parseFloat(rm);  form.elements[2].value = p;
        q = rp - rm; form.elements[3].value = q;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( p !="" && q !="" )  {
        a = Math.sqrt(parseFloat(p*p)+parseFloat(q*q))/2;  form.elements[0].value = a;
        h = p*q/(2*a); form.elements[1].value = h;
        S = a*h; form.elements[4].value = S;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( p !="" && h !="" )  {
        var pp = p*p;
        a = 0.5*pp/Math.sqrt(pp-h*h);  form.elements[0].value = a;
        S = a*h; form.elements[4].value = S;
        q = Math.sqrt(4*a*a-pp); form.elements[3].value = q;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( q !="" && h !="" )  {
        var qq = q*q;
        a = 0.5*qq/Math.sqrt(qq-h*h);  form.elements[0].value = a;
        S = a*h; form.elements[4].value = S;
        p = Math.sqrt(4*a*a-qq); form.elements[2].value = p;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( a !="" && S !="" )  {
        h = S/a; form.elements[1].value = h;
        var aa = a*a,  
                rp = Math.sqrt(parseFloat(aa)+parseFloat(S) ),
                rm = Math.sqrt(parseFloat(aa)-parseFloat(S) );
        p = parseFloat(rp)+parseFloat(rm);  form.elements[2].value = p;
        q = rp - rm; form.elements[3].value = q;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( p !="" && S !="" )  {
        q = 2*S/p; form.elements[3].value = q;
        a = Math.sqrt(parseFloat(p*p)+parseFloat(q*q))/2;  form.elements[0].value = a;
        h = p*q/(2*a); form.elements[1].value = h;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( q !="" && S !="" )  {
        p = 2*S/q; form.elements[2].value = p;
        a = Math.sqrt(parseFloat(p*p)+parseFloat(q*q))/2;  form.elements[0].value = a;
        h = p*q/(2*a); form.elements[1].value = h;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
    else if ( S !="" && h !="" )  {
        a = S/h; form.elements[0].value = a;
        var aa = a*a,  
                rp = Math.sqrt(parseFloat(aa)+parseFloat(S) ),
                rm = Math.sqrt(parseFloat(aa)-parseFloat(S) );
        p = parseFloat(rp)+parseFloat(rm);  form.elements[2].value = p;
        q = rp - rm; form.elements[3].value = q;
        C = 4*a; form.elements[6].value = C;
        r = h/2; form.elements[7].value = r;
    }
}


function circle(form) {
    if (form.elements[0].value =="") alert("Please fill in the first box.");
    var r =form.elements[0].value;
    form.elements[2].value = 2*Math.PI*r;
    form.elements[3].value = r*Math.PI*r;
    form.elements[4].value = 4*r*Math.PI*r;
    form.elements[5].value = 4/3*r*r*Math.PI*r;
}

function cirseg(form) {
    var r = form.elements[0].value, 
        h = form.elements[1].value,
        s = form.elements[2].value,
        a = form.elements[3].value,
        thi = form.elements[4].value, 
        l = form.elements[15].value, b;
     //alert('a='+a+", b="+b+", h="+h+", s="+s);  
    if ( h !="" )  {
        b = r-h;  
        a = 2*Math.sqrt(r*r-b*b); form.elements[3].value = a;
        thi = 2*Math.acos(b/r); form.elements[4].value = thi;
        s = r*thi; form.elements[2].value = s;
    }  
    else if ( s !="" )  {
        thi = s/r; form.elements[4].value = thi;
        b = r*Math.cos(thi/2); 
        h = r-b; form.elements[1].value =h; 
        a = 2*r*Math.sin(thi/2); form.elements[3].value = a;
    } 
    
    else if ( a !="" )  {
        thi = 2*Math.asin(0.5*a/r); form.elements[4].value = thi;
        b = r*Math.cos(thi/2); 
        h = r-b; form.elements[1].value = h; 
        s = r*thi; form.elements[2].value = s;
    }
    else if ( thi !="" )  {
        s = r*thi; form.elements[2].value = s;
        a = 2*r*Math.sin(thi/2); form.elements[3].value = a;
        b = r*Math.cos(thi/2); 
        h = r-b; form.elements[1].value = h; 
    }
    form.elements[6].value = parseFloat(s)+parseFloat(a); //c1
    form.elements[7].value = 0.5*(r*s-a*b); //A1
    form.elements[8].value = parseFloat(s)+parseFloat(2*r);
    form.elements[9].value = r*s/2;
    form.elements[10].value = 2*Math.PI*r*h; //Curve area
    form.elements[11].value = parseFloat(form.elements[10].value)+0.25*Math.PI*a*a; //s1
    form.elements[12].value = Math.PI*h*h*(3*r-h)/3; // V1
    form.elements[13].value = Math.PI*r*(2*h+0.5*a); //s2
    form.elements[14].value = 2*Math.PI*r*r*h/3; //V2
    form.elements[16].value = l*form.elements[6].value; //tanker surface
    form.elements[17].value = l*form.elements[7].value; //tanker volume
}

function prism(form) {
    if (form.elements[0].value ==""||form.elements[1].value ==""||form.elements[2].value =="") 
        alert("Please fill in the first 3 boxes.");
    
    var     a = parseFloat(form.elements[0].value),
            b = parseFloat(form.elements[1].value),
            c = parseFloat(form.elements[2].value);
    if ( op == 'prism') {
    form.elements[3].value = 2*(a*b+b*c+a*c);
    form.elements[4].value = a*b*c;}
    else {
    var l1=Math.sqrt(c*c+0.25*a*a), l2=Math.sqrt(c*c+0.25*b*b);
    form.elements[3].value = l1*b+a*l2+a*b;
    form.elements[4].value = a*b*c/3;
    }
}

function cylinder(form) {
    if (form.elements[0].value ==""||form.elements[1].value =="") 
        alert("Please fill in the first 2 boxes.");
    
    var     r = parseFloat(form.elements[0].value),
            h = parseFloat(form.elements[1].value);
    if ( op == 'cyl') {
    form.elements[2].value = 2*Math.PI*r*(h+r);
    form.elements[3].value = Math.PI*r*r*h;}
    else {
    var l=Math.sqrt(r*r+h*h);
    form.elements[2].value = Math.PI*r*(l+r);
    form.elements[3].value = Math.PI*r*r*h/3;
    }
}

function hollowcyl(form) {
    if (form.elements[0].value =="" || form.elements[1].value =="" || form.elements[2].value =="")
        alert("Please fill in the first box.");
    var r1 =form.elements[0].value, r2 =form.elements[1].value, h =form.elements[2].value;
    var c = 2*Math.PI*(parseFloat(r1)+parseFloat(r2)), s = Math.PI*(r1*r1-r2*r2);
    form.elements[6].value = c;
    form.elements[7].value = s;
    form.elements[3].value = parseFloat(c*h)+2*s;
    form.elements[4].value = s*h;
}



