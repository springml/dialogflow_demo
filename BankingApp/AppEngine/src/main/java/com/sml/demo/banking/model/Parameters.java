package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */
public class Parameters
{
    private String query;

    private String userId;

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
