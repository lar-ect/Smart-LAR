#define F_CPU 16000000UL

#include <avr/io.h>
// #include <util/delay.h>
#include <avr/interrupt.h>


#define set_bit(Y, bit_x) (Y|=(1<<bit_x))
#define clr_bit(Y, bit_x) (Y&=~(1<<bit_x))
#define cpl_bit(Y, bit_x) (Y^=(1<<bit_x))
#define tst_bit(Y, bit_x)  (Y&(1<<bit_x))

#define LED PC5

uint8_t counter = 0x00;
uint8_t state = 0x00;




void setup() {
  // put your setup code here, to run once:

   DDRC = 0xFF;

	cli();
	
		TCNT0 = 0b00000000;
		TCCR0B = 0b0000011;
		TIMSK0 = 0b0000001; // 0b00000001 
	sei();
   

}

void pisca(){
	if( tst_bit(PORTD, LED) ){
		clr_bit(PORTB, LED);
	}else{
		clr_bit(PORTB, LED);	
	}
}


ISR(TIMER0_OVF_Vect){	
	counter++;
	if(counter == 1000){
		counter = 0;
		pisca();
	}
}



void loop() {
  // put your main code here, to run repeatedly:

}
