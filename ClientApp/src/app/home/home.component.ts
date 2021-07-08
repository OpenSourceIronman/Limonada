import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { AbstractControl, FormBuilder, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { KaypadComponent } from 'src/app/kaypad/kaypad.component';
import * as moment from 'moment';
import { Subscription } from 'rxjs';
import { finalize } from 'rxjs/operators';

export function AgeValidator(control: AbstractControl): { [key: string]: boolean } | null {
  const today = new Date();
  const birthDate = new Date(control.value);
  let age = today.getFullYear() - birthDate.getFullYear();
  const m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
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
  private date_picker_subcription: Subscription;
  public age = 0;
  public today = new Date();
  public show_error: boolean = false;
  public shake_error: boolean = false;
  private dialogRef: MatDialogRef<any> = null;
  private dateExp = /^((0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2})*$/;
  public date_picker = new FormControl(null, [Validators.required, Validators.pattern(this.dateExp)]);


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

  constructor(private _formBuilder: FormBuilder , private router:Router, private dialog: MatDialog) {
  }

  ngOnInit(){
    // this.date_picker_subcription = this.date_picker.valueChanges.subscribe((value)=>{
      
    //   // let val = moment(value).format('MM/DD/YYYY');

    //   // if date matach to pattern then calulate age
    //   // if(this.date_regex.test(val)){
    //   //   this.show_error = false;
    //   //   let user_age = moment(`${val}`);
    //   //   let today = moment();
    //   //   this.age = today.diff(user_age, 'years');
    //   // } else {
    //   //   this.show_error = true;
    //   // }
    // })
  }

  ngOnDestroy(){
    this.date_picker_subcription.unsubscribe();
  }


  gotoSecondPage(){
    this.router.navigateByUrl('/second');
  }

  openKeypad(){
    if(!this.dialogRef){
      this.dialogRef = this.dialog.open(KaypadComponent, {
        position: {
          bottom: '0px'
        },
        minWidth: '100%',
        data: this.date_picker,
        autoFocus: false,
        hasBackdrop: false
      });

      this.date_picker_subcription = this.dialogRef.afterClosed().pipe(
        finalize(() => this.dialogRef = null)
      ).subscribe(()=>{
        this.shake_error = false;
        this.show_error = false;
        if(this.dateExp.test(this.date_picker.value)){
          let val = moment(this.date_picker.value).format('MM/DD/YYYY');
          this.show_error = false;
          let user_age = moment(`${val}`);
          let today = moment();
          this.age = today.diff(user_age, 'years');
          if(this.age >= 21){
            setTimeout(()=>{
              this.gotoSecondPage();
              if(this.dialogRef){
                this.dialogRef.close();
              }
            }, 2500);
          } else {
            this.show_error = true;
          }
        } else {
          this.show_error = true;
          this.shake_error = true;
        }
      });
    }

  }
}
