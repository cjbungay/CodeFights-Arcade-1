function maxMultiple(divisor::Int32, bound::Int32)
    return bound % (bound % divisor)
end