package com.sml.demo.banking.util;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class CommonUtil {
    public static String random(int size) {

        StringBuilder generatedToken = new StringBuilder();
        try {
            SecureRandom number = SecureRandom.getInstance("SHA1PRNG");
            // Generate 20 integers 0..20
            for (int i = 0; i < size; i++) {
                if(i==0){
                    generatedToken.append(9);
                }
                else {
                    generatedToken.append(number.nextInt(9));
                }
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        return generatedToken.toString();
    }

}
