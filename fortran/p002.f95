! Even Fiboonacci Numbers

module data
implicit none
    integer :: fibs, LIMIT = 4000000
    integer, dimension(:), allocatable :: table

    contains
    subroutine initialise
        fibs = ceiling(log(LIMIT * 5**0.5) / log(0.5 * (1 + 5**0.5)))
        allocate(table(fibs))
    end subroutine initialise
end module data


recursive integer function fibonacci(n) result(res)
use data, only : table
implicit none
    integer :: n

    if (n == 1) then
        table(1) = 1
    else if (n == 2) then
        table(2) = 2
    else if (table(n) == 0) then
        table(n) = fibonacci(n - 1) + fibonacci(n - 2)
    endif
    res = table(n)
end function fibonacci


integer function solve()
use data, only : fibs, LIMIT, table
implicit none
    integer :: i, x, fibonacci

    solve = 0
    do i = 2, fibs, 3
        x = fibonacci(i)
        if (x < LIMIT) then
            solve = solve + x
        endif
    end do
end function solve


program p002
use data, only : initialise
implicit none
    integer :: x, solve
    
    call initialise
    print *, solve()
end program p002
