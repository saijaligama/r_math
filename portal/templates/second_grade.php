<?php include("header.php"); ?>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> Second Grade EOG</title>

    <link rel="stylesheet" type="text/css" href="/uncg_math/static/Geometry_files/mystyle.css">
    <meta name="description" content="Regular polygon, Trangle,
              Quadrilateral, Rectangle, Rombus, Trapezoid,
              Circle, Circular Segment/Sector, Prism, Pyramid,
              Cylinder, Cone, Sperical Cap/Sector">
    <script src="/uncg_math/static/Geometry_files/geometry.js"></script>
<style>
    .text_box_st {
        padding: 1px !important;
        width: 90px !important;
    }

    .text_box_st2 {
        padding: 3px !important;
        width: 90px !important;
    }
</style>
</head>


    <div class="example" style="height: 100% !important;">
        <div id="nav" style="clear:both;">
            <h1 style="color: white;text-align: center;"> EOG Tests </h1>

            <ul style="margin-top: -20px;">
                <li style="padding-left: 179px;"><a href="/uncg_math">Home</a></li>

            </ul>
            
        </div>
<h2 style="text-align:center">Second Grade EOG 1</h2>
<input type="button" class="btn btn-success" value="Open Question Steet" onClick="window.open('question/2014_2015_2nd_Mid_Year_Student_Booklet.pdf');">
<form action="" method="POST">
    <button style="margin-top: -34px;margin-left: 171px;" class="btn btn-info" name="click" class="click">Start Test</button>
</form>
<?php
if(isset($_POST['click']))
{
  $date_clicked = time();
  //  $date_clicked = date('Y-m-d H:i:s');
	echo "You can Fill Box Now";
	
}?>

<form action="/uncg_math/templates/kindergarden_answer.php" method="POST">
<table border=0 width=100% bgcolor=moccasin>

<div class='col-md-6'>
<tr>
<td>
<h3>Task1</h3>
<div style="margin-left:5%">
<h3>1</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'>&nbsp;&nbsp;Inches<br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'>&nbsp;&nbsp;Inches<br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'>&nbsp;&nbsp;Inches<br><br/>
d&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='2'>&nbsp;&nbsp;Inches<br><br/>
</div>
<h3>2</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Inches<br><br/>
</div>
</div>
</td>
</tr>

<tr>
<td>
<h3>Task2</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>Feet<br><br/>
</div>
</tr>
</td>


<tr>
<td>
<h3>Task3</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Inches<br><br/>
</div>

</tr>
</td>



<tr>
<td>
<h3>Task4</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Ducks<br><br/>
</div>
</tr>
</td>



<tr>
<td>
<h3>Task5</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Flower<br><br/>
</div>
</td>
</tr>


<tr>
<td>
<h3>Task6</h3>
<div style="margin-left:5%">
<h3>Part 1</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='4' size='2'>&nbsp;&nbsp;Eraser<br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='10' size='2'><br><br/>
</div>
<h3>Part 2</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='30' size='2'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='35' size='2'><br><br/>
</div></div>

</td>
</tr>



<tr>
<td>
<h3>Task7</h3>
<div style="margin-left:5%">
<h3>Part 1</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='25' size='2'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
d&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
e&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='15' size='2'><br><br/>
f&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
g&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
</div>

</div></div><div class='col-md-6'>

</div></div><div class='col-md-6'>


<h3>Part 2</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
d&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
</div>
</td>
</tr>

<tr>
<td>
<h3>Task8</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
</div>
</td>
</tr>


<tr>
<td>
<h3>Task9</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
</div>

</td>
</tr>

<tr>
<td>
<<h3>Task10</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
</div>

</tr>
</td>


<tr>
<td>
<h3>Task11</h3>
<div style="margin-left:5%">
<h3>Part 1</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='25' size='10'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='14' size='10'><br><br/>
</div>
<h3>Part 2</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='100' size='50'><br><br/>
</div>

<h3>Part 3</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
d&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
e&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
f&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
g&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
h&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
</div>

</td>
</tr>

</table>
<input type='hidden' name='stime' value="<?php echo $date_clicked;?>">
    <button name="res" class="big btn btn-primary">Submit Answer</button>
</form>
