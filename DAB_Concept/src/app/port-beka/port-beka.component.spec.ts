import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PortBekaComponent } from './port-beka.component';

describe('PortBekaComponent', () => {
  let component: PortBekaComponent;
  let fixture: ComponentFixture<PortBekaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PortBekaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PortBekaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
