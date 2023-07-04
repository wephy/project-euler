! Multiples of 3 and 5

integer function solve()
implicit none
    integer :: i

    solve = 0
    do i = 1, 999
        if (mod(i, 3) == 0 .or. mod(i, 5) == 0) then
            solve = solve + i
        end if
    end do
end function solve


program p001
implicit none
    integer :: solve

    print *, solve()
end program p001
