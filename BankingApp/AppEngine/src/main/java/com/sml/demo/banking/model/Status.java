package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */
public class Status
{
    private String errorType;

    private String code;

    public String getErrorType ()
    {
        return errorType;
    }

    public void setErrorType (String errorType)
    {
        this.errorType = errorType;
    }

    public String getCode ()
    {
        return code;
    }

    public void setCode (String code)
    {
        this.code = code;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [errorType = "+errorType+", code = "+code+"]";
    }
}
