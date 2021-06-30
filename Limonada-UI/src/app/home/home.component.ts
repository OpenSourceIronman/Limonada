import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { MatDatepickerInputEvent } from '@angular/material';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  date = new FormControl(new Date());
  value: Date = new Date();
  getYear : any;
  checkDate : Date;
  form : FormGroup;
  isShow : boolean;
  constructor(private fb: FormBuilder , private router:Router ) {
    this.form = this.fb.group({
      format1: new FormControl(new Date()),
      format2: new FormControl(new Date())
    });
  }
  onChangeEvent(event: any) {
    debugger
    var data = event.target.value;
    if (data >= 18) {
      this.isShow = true;
    }
    else {
      this.isShow = false;
    }
    return this.isShow;
  }
  btnClick= function () {
    if(this.isShow==true){
      this.router.navigateByUrl('/second');
    }

};
  // addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
  //   debugger
  //   this.checkDate = event.target.value;
  //   this.getYear = this.checkDate;

  // }
}
