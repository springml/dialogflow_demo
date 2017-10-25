package com.sml.demo.banking;

import com.sml.demo.banking.security.OtpManager;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
    @Bean
    public BankingService bankingService() {
        return new BankingService();
    }

    @Bean
    public OtpManager otpManager() {
        return new OtpManager();
    }

}
