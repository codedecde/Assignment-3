(define (problem car_parking)
(:domain car_park)
(:objects car-1 car-2 car-3 car-4 car-5 car-6 car-7 car-8  - car
	sq-0 sq-1 sq-2 sq-3 sq-4 sq-5 sq-6 sq-7 sq-8 sq-9 sq-10 sq-11 sq-12 sq-13 sq-14 sq-15 sq-16 sq-17 sq-18 sq-19 sq-20 sq-21 sq-22 sq-23 sq-24 sq-25 sq-26 sq-27 sq-28 sq-29 sq-30 sq-31 sq-32 sq-33 sq-34 sq-35  - pos)
(:init (is_empty sq-0) (is_empty sq-2) (is_empty sq-6) (is_empty sq-8) (is_empty sq-9) (is_empty sq-10) (is_empty sq-11) (is_empty sq-12) (is_empty sq-14) (is_empty sq-17) (is_empty sq-18) (is_empty sq-19) (is_empty sq-28) (is_empty sq-29) (is_empty sq-32) (is_empty sq-34) (is_empty sq-35) 
	(loc_car car-1 sq-15 sq-16) (loc_car car-2 sq-1 sq-13) (loc_car car-3 sq-3 sq-5) (loc_car car-4 sq-20 sq-26) (loc_car car-5 sq-24 sq-25) (loc_car car-6 sq-30 sq-31) (loc_car car-7 sq-27 sq-33) (loc_car car-8 sq-21 sq-23) 
	(left_adj sq-0 sq-1) (left_adj sq-1 sq-2) (left_adj sq-2 sq-3) (left_adj sq-3 sq-4) (left_adj sq-4 sq-5) (left_adj sq-6 sq-7) (left_adj sq-7 sq-8) (left_adj sq-8 sq-9) (left_adj sq-9 sq-10) (left_adj sq-10 sq-11) (left_adj sq-12 sq-13) (left_adj sq-13 sq-14) (left_adj sq-14 sq-15) (left_adj sq-15 sq-16) (left_adj sq-16 sq-17) (left_adj sq-18 sq-19) (left_adj sq-19 sq-20) (left_adj sq-20 sq-21) (left_adj sq-21 sq-22) (left_adj sq-22 sq-23) (left_adj sq-24 sq-25) (left_adj sq-25 sq-26) (left_adj sq-26 sq-27) (left_adj sq-27 sq-28) (left_adj sq-28 sq-29) (left_adj sq-30 sq-31) (left_adj sq-31 sq-32) (left_adj sq-32 sq-33) (left_adj sq-33 sq-34) (left_adj sq-34 sq-35) 
	(is_H car-1) (is_V car-2) (is_H car-3) (is_V car-4) (is_H car-5) (is_H car-6) (is_V car-7) (is_H car-8) 
	(right_adj sq-1 sq-0) (right_adj sq-2 sq-1) (right_adj sq-3 sq-2) (right_adj sq-4 sq-3) (right_adj sq-5 sq-4) (right_adj sq-7 sq-6) (right_adj sq-8 sq-7) (right_adj sq-9 sq-8) (right_adj sq-10 sq-9) (right_adj sq-11 sq-10) (right_adj sq-13 sq-12) (right_adj sq-14 sq-13) (right_adj sq-15 sq-14) (right_adj sq-16 sq-15) (right_adj sq-17 sq-16) (right_adj sq-19 sq-18) (right_adj sq-20 sq-19) (right_adj sq-21 sq-20) (right_adj sq-22 sq-21) (right_adj sq-23 sq-22) (right_adj sq-25 sq-24) (right_adj sq-26 sq-25) (right_adj sq-27 sq-26) (right_adj sq-28 sq-27) (right_adj sq-29 sq-28) (right_adj sq-31 sq-30) (right_adj sq-32 sq-31) (right_adj sq-33 sq-32) (right_adj sq-34 sq-33) (right_adj sq-35 sq-34) 
	(top_adj sq-0 sq-6) (top_adj sq-1 sq-7) (top_adj sq-2 sq-8) (top_adj sq-3 sq-9) (top_adj sq-4 sq-10) (top_adj sq-5 sq-11) (top_adj sq-6 sq-12) (top_adj sq-7 sq-13) (top_adj sq-8 sq-14) (top_adj sq-9 sq-15) (top_adj sq-10 sq-16) (top_adj sq-11 sq-17) (top_adj sq-12 sq-18) (top_adj sq-13 sq-19) (top_adj sq-14 sq-20) (top_adj sq-15 sq-21) (top_adj sq-16 sq-22) (top_adj sq-17 sq-23) (top_adj sq-18 sq-24) (top_adj sq-19 sq-25) (top_adj sq-20 sq-26) (top_adj sq-21 sq-27) (top_adj sq-22 sq-28) (top_adj sq-23 sq-29) (top_adj sq-24 sq-30) (top_adj sq-25 sq-31) (top_adj sq-26 sq-32) (top_adj sq-27 sq-33) (top_adj sq-28 sq-34) (top_adj sq-29 sq-35) 
	(bottom_adj sq-6 sq-0) (bottom_adj sq-7 sq-1) (bottom_adj sq-8 sq-2) (bottom_adj sq-9 sq-3) (bottom_adj sq-10 sq-4) (bottom_adj sq-11 sq-5) (bottom_adj sq-12 sq-6) (bottom_adj sq-13 sq-7) (bottom_adj sq-14 sq-8) (bottom_adj sq-15 sq-9) (bottom_adj sq-16 sq-10) (bottom_adj sq-17 sq-11) (bottom_adj sq-18 sq-12) (bottom_adj sq-19 sq-13) (bottom_adj sq-20 sq-14) (bottom_adj sq-21 sq-15) (bottom_adj sq-22 sq-16) (bottom_adj sq-23 sq-17) (bottom_adj sq-24 sq-18) (bottom_adj sq-25 sq-19) (bottom_adj sq-26 sq-20) (bottom_adj sq-27 sq-21) (bottom_adj sq-28 sq-22) (bottom_adj sq-29 sq-23) (bottom_adj sq-30 sq-24) (bottom_adj sq-31 sq-25) (bottom_adj sq-32 sq-26) (bottom_adj sq-33 sq-27) (bottom_adj sq-34 sq-28) (bottom_adj sq-35 sq-29) )
(:goal (loc_car car-1 12 13))
)