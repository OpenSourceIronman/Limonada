import { Directive, HostListener, Input} from '@angular/core';
import { FormControl } from '@angular/forms';

const ALLOWED_KEYS = [
  'Tab',
  'Backspace',
  'Delete',
  'ArrowUp',
  'ArrowRight',
  'ArrowDown',
  'ArrowLeft',
  'Home',
  'End',
  'Control'
];

@Directive({
  selector: '[appDateInputFormatter]'
})

export class DateInputFormatterDirective {

  @Input() appDateInputFormatter: FormControl;
  private _allowedKeys = ALLOWED_KEYS;
  constructor() { }

  @HostListener('keyup', ['$event'])
  private _onKeyup(event: KeyboardEvent): void {
    if (this._allowedKeys.includes(event.key)) {
      return;
    } else {
      let current = this.appDateInputFormatter.value; 
      if (!current) {
        return null;
      }
  
      current = current.replace(/\/+/, '/');
  
      if (/^\d{2}(\/\d{2})?$/.test(current)) {
        current =  current + '/';
      }
  
      this.appDateInputFormatter.setValue(current);
    }
  }

}
