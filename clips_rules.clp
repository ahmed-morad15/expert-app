(deftemplate patient
    (slot age)
    (slot bmi)
    (slot glucose)
    (slot hypertension (default "no"))
    (slot smoking (default "no"))
    (slot diabetes (default "unknown"))
)

; ================= HIGH RISK =================
(defrule high_risk
   ?fact <- (patient (age ?age) 
                     (bmi ?bmi) 
                     (glucose ?glucose))
   (test (and (>= ?age 45) 
              (>= ?bmi 30) 
              (>= ?glucose 126)))
   =>
   (modify ?fact (diabetes "high risk"))
)

; ================= MEDIUM RISK =================
(defrule medium_risk
   ?fact <- (patient (age ?age) 
                     (bmi ?bmi) 
                     (glucose ?glucose))
   (test (and (>= ?age 35) (<= ?age 44)
              (>= ?bmi 25) (<= ?bmi 29)
              (>= ?glucose 110) (<= ?glucose 125)))
   =>
   (modify ?fact (diabetes "medium risk"))
)

; ================= LOW RISK =================
(defrule low_risk
   ?fact <- (patient (age ?age) 
                     (bmi ?bmi) 
                     (glucose ?glucose))
   (test (and (< ?age 35) 
              (< ?bmi 25) 
              (< ?glucose 110)))
   =>
   (modify ?fact (diabetes "low risk"))
)
