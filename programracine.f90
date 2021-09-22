! calcul de la suite de Fibonacci
recursive function fib(n) result(f)
    integer, intent (in) :: n
    integer :: f

    if (n==1 .or. n==2) then
        f = 1
    else
        f = fib(n-1)+fib(n-2)
    endif
end function fib

program fibonacci
integer :: n
integer :: i
integer :: fib
character(8)    :: arg_n

call getarg(1,arg_n)
read(arg_n,*) n
do i=1,n
    print*, fib(i)
enddo
end program fibonacci