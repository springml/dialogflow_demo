package com.sml.demo.banking;

import com.sml.demo.banking.model.WebhookRequest;
import com.sml.demo.banking.model.WebhookResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


/**
 * Created by kaarthikraaj on 9/8/17.
 */
@RestController
public class BankingServiceController {

    @Autowired
    BankingService bankingService ;
    @CrossOrigin
    @RequestMapping(value = "/sendAuthCode", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<WebhookResponse> sendSMS(String userId) {
        System.out.println("The request is received");
        boolean isValid = false;
        WebhookResponse response = null;
        try {
             response = bankingService.sendAuthCode(userId);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/getAccBalance", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<WebhookResponse> getAccBalance(String userId,String otp) {
        System.out.println("The request is received");
        boolean isValid = false;
        WebhookResponse response = null;
        try {
            response = bankingService.getAccBalance(userId,otp);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/createAccountForUser", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<String> createAccountForUser(String userId) {
        System.out.println("The request is received");
        boolean isValid = false;
        String response = "";
        try {
            response = bankingService.createAccountForUser(userId);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/registerUser", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<String> resgisterUser(String userId,String mobile,String email) {
        System.out.println("The request is received for mobile"+mobile);
        boolean isValid = false;
        String response = "";
        try {
            response = bankingService.addUser(userId,mobile,email);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/creditAccount", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<String> creditAccount(String userId,long amt) {
        System.out.println("The request is received");
        boolean isValid = false;
        String response = "";
        try {
            response = bankingService.creditAmountForUser(userId,amt);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/debitAccount", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<String> debitAccount(String userId,long amt) {
        System.out.println("The request is received");
        boolean isValid = false;
        String response = "";
        try {
            response = bankingService.debitAmountForUser(userId,amt);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/requestBankOperationbackup", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<WebhookResponse> doBankOperationBackUp(String userId,String query,String otp) {
        System.out.println("The userId retreved is "+ userId+" the query is "+query + " the otp is "+otp);
        WebhookResponse response = null;
        switch(query) {
            case "authenticateUser":
              response  = bankingService.sendAuthCode(userId);
              break;
            case "getAccBalance":
                response = bankingService.getAccBalance(userId, otp);
        }
        return ResponseEntity.ok(response);
    }

    @CrossOrigin
    @RequestMapping(value = "/requestBankOperation", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<WebhookResponse> doBankOperation(@RequestBody WebhookRequest request) {
        String userId = request.getResult().getParameters().getUserId();
        String query = request.getResult().getParameters().getQuery();
        String otp = request.getResult().getParameters().getOtp();

        System.out.println("The userId retreved is "+ userId+" the query is "+query + " the otp is "+otp);
        WebhookResponse response = null;
        switch(query) {
            case "authenticateUser":
                response  = bankingService.sendAuthCode(userId);
                break;
            case "getAccBalance":
                response = bankingService.getAccBalance(userId, otp);
        }
        return ResponseEntity.ok(response);
    }



}
