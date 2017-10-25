package com.sml.demo.banking.account;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class Account {
    long balance;
    String accNumber;

    public String getAccNumber() {
        return accNumber;
    }

    public void setAccNumber(String accNumber) {
        this.accNumber = accNumber;
    }

    public long getBalance() {
        return balance;
    }

    public void setBalance(long balance) {
        this.balance = balance;
    }

    public void creditAccount(long amount){
        balance+=amount;
    }

    public void debitAccount(long amount){
        balance-=amount;
    }
}
