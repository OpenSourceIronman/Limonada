import { Component, OnInit, Inject } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-kaypad',
  templateUrl: './kaypad.component.html',
  styleUrls: ['./kaypad.component.css']
})
export class KaypadComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<KaypadComponent>, @Inject(MAT_DIALOG_DATA) public data: FormControl) { }

  ngOnInit() {
  }

  setNumber(number: string){

    let current: string = this.data.value; 
    current = `${current+number}`;
    // console.log(current)
    current = current.replace(/\/+/, '/');
    if (/^\d{2}(\/\d{2})?$/.test(current)) {
      current =  current + '/';
    }
    if(current.length > 10){
      current = current.substring(0, current.length-1);
    }
    this.data.setValue(current);
  }

  backspace(){
    let value: string = this.data.value;
    value = value.substring(0, value.length-1);
    this.data.setValue(`${value}`);
  }

  done(){
    this.dialogRef.close();
  }
  

}
