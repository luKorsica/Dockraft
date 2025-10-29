import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServSettings } from './serv-settings';

describe('ServSettings', () => {
  let component: ServSettings;
  let fixture: ComponentFixture<ServSettings>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ServSettings]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ServSettings);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
