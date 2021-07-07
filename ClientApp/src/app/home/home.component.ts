import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { AbstractControl, FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import {  ErrorStateMatcher, MatDatepickerInputEvent } from '@angular/material';
import { Router } from '@angular/router';

import * as moment from 'moment';
import { Subscription } from 'rxjs';

export function AgeValidator(control: AbstractControl): { [key: string]: boolean } | null {
  const today = new Date();
  const birthDate = new Date(control.value);
  let age = today.getFullYear() - birthDate.getFullYear();
  const m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  // debugger

  if (age < 21) {
    return { 'age': true };
  }
  return null;
}
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit, OnDestroy {
  private date_regex = /^((0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2})*$/;
  private date_picker_subcription: Subscription;
  public age = 0;
  date_picker = new FormControl(null, Validators.required);
  public today = new Date();
  public show_error: boolean = false;


// oldcode

  // events: string[] = [];
  // isShow:boolean;
  // addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
  //   debugger
  //   this.events.push(`${type}: ${event.value}`);
  //   let selectedDate = event.value;
  //   const today = new Date();
  //   const birthDate = new Date(selectedDate);
  //   let age = today.getFullYear() - birthDate.getFullYear();
  //   const m = today.getMonth() - birthDate.getMonth();
  //   debugger
  //   if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
  //     age--;
  //   }

  //   if (age >= 18) {
  //     this.isShow = true;
  //   }
  //   else {
  //     return  this.isShow = false;
  //   }
  //   return this.isShow;
  // }

  // oldcode

  constructor(private _formBuilder: FormBuilder , private router:Router ) {
  }

  ngOnInit(){
    this.date_picker_subcription = this.date_picker.valueChanges.subscribe((value)=>{
      let val = moment(value).format('MM/DD/YYYY');
      // if date matach to pattern then calulate age
      if(this.date_regex.test(val)){
        this.show_error = false;
        let user_age = moment(`${val}`);
        let today = moment();
        this.age = today.diff(user_age, 'years');
      } else {
        this.show_error = true;
      }
    })
  }

  ngOnDestroy(){
    this.date_picker_subcription.unsubscribe();
  }

  
// unused code / old code
  validatorForm = this._formBuilder.group({
    dob:['', [Validators.required, AgeValidator]]
    // name:['',Validators.required]
  })
  get dob() {
    return this.validatorForm.get('dob');
  }
  public hasError = (controlName: string, errorName: string) => {
    return this.validatorForm.controls[controlName].hasError(errorName);
  }
  btnClick = function () {
    // debugger
    if (this.validatorForm.valid) {
      console.log(this.validatorForm.value)
      this.router.navigateByUrl('/second');
    }
  };
  // unused code / old code

  gotoSecond(){
    this.router.navigateByUrl('/second');
  }
}
