# To run: download RARS - https://github.com/TheThirdOne/rars/releases
# To run, command after downloading RARS: java -jar ~/Downloads/rars1_6.jar nc me cracklepop.s > result.txt
.global _boot
.text
#t0: i
#t1: n
#t2: total
#t3: intermediary for calculations
#t4: intermediary for comparison
_boot:
# for (int i = 1; i < 100; i = i+1), make sure inclusive for 1 and 100 /
  li		t0, 1
  li 		t1, 100
  j 		_forLoop 

# beqz for branch if t4 is 0 
_forLoop:
  
  li            t3, 15
  rem           t4, t0, t3
  beqz          t4,  _printCracklePop

  li		t3, 3
  rem		t4, t0, t3 
  beqz		t4, _printCrackle 

  li		t3, 5
  rem		t4, t0, t3
  beqz		t4,  _printPop 
  
  j		_printNumber 

_forLoopNext:
  # Incrementing i and loop. Checks if i <= n
  addi	t0, t0, 1
  ble 	t0, t1, _forLoop
  
  #10 is the value for terminating a process aka when the program is done.
  #a7 is used for calling the syscall number (10) here 
  li 	a7, 10 
  ecall 

  #  printing the word (Crackle, Pop, or CracklePop)
  # if n (t0) is divisible by 3, print Crackle
  # system call will always be a7, and then 4 is for address of string 
  # a0 is always used to pass a string to as the first value in an argument. This is actually for something
  # similar to passing any parameter value. I.e: a3 is for the fourth argument. Goes up to a0-a7 
  # we always use j _forLoopNext to go back to the loop after the conditional checks
  # a7, 1 is sets the syscall code aka 1 for printing an integer 
  # a0, 10 puts a new line 
  # a7, 11 is the Print Character operation 
_printNumber:
  mv a0, t0
  li a7, 1
  ecall 
 
  li a0, 10 
  li a7, 11 
  ecall 
  j _forLoopNext 

_printCrackle:
  la a0, crackle_str
  li a7, 4
  ecall
  j _forLoopNext

_printPop:
  la a0, pop_str
  li a7, 4
  ecall
  j _forLoopNext

_printCracklePop:
  la a0, cracklepop_str
  li a7, 4
  ecall
  j _forLoopNext
.data
variable:
  crackle_str: .asciz "Crackle\n"
  pop_str: .asciz "Pop\n"
  cracklepop_str: .asciz "CracklePop\n"
