student = ["Taha khan", "Khubaib hanif", "Ahsan siddique", "Hassan afzal"];
fathersname =["Khan", "Hanif", "Siddique", "Afzal"];

for (let i=0; i<student.length; i++){
    for(let j=0; j<fathersname.length; i++){
        position = student[i].split(' ');
        if (position[1] == fathersname[j]){
            //console.log( `${element} 's father name found at index' ${i}`)
            console.log(student[i] + "last name found at index: " + j);
        }
    }
}