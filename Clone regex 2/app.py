from flask import Flask ,render_template,request
import re
app=Flask(__name__)
################################################
@app.route('/', methods=['GET', 'POST'])
def regex():
    if request.method=='POST':
         text_string=request.form['string']
         regex_string=request.form['reg_string']
         no_of_search= re.findall(regex_string,text_string)
         return render_template('1.html',cnt=len(no_of_search),str1=text_string,reg1=regex_string)
    return render_template('1.html')

################################################
if __name__=='__main__':
    app.run(debug=True)