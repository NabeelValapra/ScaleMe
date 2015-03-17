function beforeCheck() { 
    console.log('Sample form validated before sending...');
    //alert('Before Check is working...!!!');
}

function showFieldError(data) {
    if(!eval(data.status)){
        errors = eval(data.error);
        $.each(errors, function(fieldname, errmsg){
          var id = "#id_" + fieldname;
          $(id).parent().after(errmsg);
        });
    }
}

function showSuccess(){
    alert('Success::Hello')
}


function cleanFieldError(data){
    // removes the field error.
} 

function formResponse(data, errorFunc=undefiened, cleanForm=false, redirect=false){
    if(data){
        if(!eval(data.status)){
            errorFunc(data);
        }else{
            // IF THE DATA FORM THE SERVER IS SAVED OR TRUE, then...
            showSuccess();
            if(eval(cleanForm)){
                // Clean the values in the form
            }
            if(eval(redirect)){
                // redirect to some url || try to use undefiened.
            }
        }
    }else{
        console.log("Data havn't recived any data to process, Please check on server.");
    }
}

