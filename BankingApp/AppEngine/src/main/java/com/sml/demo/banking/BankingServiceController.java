package com.sml.demo.banking;

import com.google.gson.Gson;
import com.sml.demo.banking.model.ContextOut;
import com.sml.demo.banking.model.Contexts;
import com.sml.demo.banking.model.WebhookRequest;
import com.sml.demo.banking.model.WebhookResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;


/**
 * Created by kaarthikraaj on 9/8/17.
 */
@RestController
public class BankingServiceController {

    @Autowired
    BankingService bankingService ;






    @CrossOrigin
    @RequestMapping(value = "/processRequest", method = RequestMethod.POST)
    public @ResponseBody
    ResponseEntity<WebhookResponse> processRequest(@RequestBody WebhookRequest request) {
        Contexts[] ctxs = request.getResult().getContexts();
        for(int i=0;i<ctxs.length;i++){
            System.out.println(ctxs[i].getName());
        }

        String userId = request.getResult().getParameters().getUserId();
        String query = request.getResult().getParameters().getQuery();
        boolean isAuthenticated = request.getResult().getParameters().isAuthenticated();

        String otp = request.getResult().getParameters().getOtp();
        String accType = request.getResult().getParameters().getAccType();
        String fromAc = request.getResult().getParameters().getFromAc();
        String toAccount = request.getResult().getParameters().getToAc();
        String mobileNumber = request.getResult().getParameters().getMobileNumber();

        long amtToTfr = request.getResult().getParameters().getTfrAmount();

        HashMap outputCtxParams = new HashMap();

        boolean validOtp = false;
        System.out.println("The userId retreved is "+ userId+" the query is "+query + " the otp is "+otp);
        System.out.println("isAuthenticatedContext param is"+isAuthenticated);
        System.out.println("acctype param is"+accType);
        System.out.println("fromAc param is"+fromAc);

        System.out.println("toAccount param is"+toAccount);
        System.out.println("amtToTfr param is"+amtToTfr);


        WebhookResponse response = null;

        if(!isAuthenticated) {
            if("".equalsIgnoreCase(otp) || otp == null) {
                response = bankingService.sendAuthCode(userId,mobileNumber);
                outputCtxParams.put("isAuthenticated", "false");
                response.getContextOut().get(0).setParameters(outputCtxParams);
                response.getContextOut().get(0).setName("balance");
                response.getContextOut().get(0).setLifespan("10");
            }
            else{
                isAuthenticated = bankingService.validateOtp(userId,otp);
            }
        }
        if(isAuthenticated){
            switch(query) {

                case "getAccBalance":
                    response = bankingService.getAccountBalance(userId,accType);
                    outputCtxParams.put("isAuthenticated","true");
                    response.getContextOut().get(0).setParameters(outputCtxParams);
                    response.getContextOut().get(0).setName("balance");
                    response.getContextOut().get(0).setLifespan("10");

                    break;
                case "transfer":
                    response = bankingService.transferBalance(userId,  fromAc, toAccount, amtToTfr);
                    outputCtxParams.put("isAuthenticated","true");
                    response.getContextOut().get(0).setParameters(outputCtxParams);
                    response.getContextOut().get(0).setName("balance");
                    response.getContextOut().get(0).setLifespan("10");

                    break;

                case "lasttransaction":
                    response = bankingService.checkLastTransaction(userId,  accType);
                    outputCtxParams.put("isAuthenticated","true");
                    response.getContextOut().get(0).setParameters(outputCtxParams);
                    response.getContextOut().get(0).setName("balance");
                    response.getContextOut().get(0).setLifespan("10");

                    break;
                case "lasttransactiondate":
                    response = bankingService.checkLastTransactionDate(userId,  accType);
                    outputCtxParams.put("isAuthenticated","true");
                    response.getContextOut().get(0).setParameters(outputCtxParams);
                    response.getContextOut().get(0).setName("balance");
                    response.getContextOut().get(0).setLifespan("10");

                    break;


            }
        }
        else{
            outputCtxParams.put("isAuthenticated","false");
            response.getContextOut().get(0).setParameters(outputCtxParams);
            response.getContextOut().get(0).setName("balance");
            response.getContextOut().get(0).setLifespan("10");
        }
        Gson gson = new Gson();
       String responsejson = gson.toJson(response);
       System.out.println(responsejson);
        return ResponseEntity.ok(response);
    }



}
