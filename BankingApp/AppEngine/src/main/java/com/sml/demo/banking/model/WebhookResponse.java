package com.sml.demo.banking.model;

import java.util.ArrayList;

/**
 * Created by kaarthikraaj on 10/8/17.
 */
public class WebhookResponse {
    private final String speech;
    private final String displayText;

    public ArrayList<ContextOut> getContextOut() {
        return contextOut;
    }

    private  ArrayList<ContextOut> contextOut = null;
    private final String source = "java-webhook";

    public void setContextOut(ArrayList<ContextOut> contextOut) {
        this.contextOut = contextOut;
    }

    public WebhookResponse(String speech, String displayText) {
        this.speech = speech;
        this.displayText = displayText;
    }

    public String getSpeech() {
        return speech;
    }

    public String getDisplayText() {
        return displayText;
    }

    public String getSource() {
        return source;
    }
}