package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */
public class Parameters
{
    private String query;

    private String userId;
    private String fromAc;
    private String toAc;
    private String accType;

    public String getAccType() {
        return accType;
    }

    public void setAccType(String accType) {
        this.accType = accType;
    }

    public String getFromAc() {
        return fromAc;
    }

    public void setFromAc(String fromAc) {
        this.fromAc = fromAc;
    }

    public String getToAc() {
        return toAc;
    }

    public void setToAc(String toAc) {
        this.toAc = toAc;
    }

    public long getTfrAmount() {
        return tfrAmount;
    }

    public void setTfrAmount(long tfrAmount) {
        this.tfrAmount = tfrAmount;
    }

    private long tfrAmount;
    public boolean isAuthenticated() {
        return authenticated;
    }

    public void setAuthenticated(boolean authenticated) {
        this.authenticated = authenticated;
    }

    private boolean authenticated;
    public String getOtp() {
        return otp;
    }

    public void setOtp(String otp) {
        this.otp = otp;
    }

    private String otp;

    public String getQuery ()
    {
        return query;
    }

    public void setQuery (String query)
    {
        this.query = query;
    }

    public String getUserId ()
    {
        return userId;
    }

    public void setUserId (String userId)
    {
        this.userId = userId;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [query = "+query+", userId = "+userId+"]";
    }
}
